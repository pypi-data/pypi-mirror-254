import os
import sys
import time
import signal
import subprocess, multiprocessing
import json
import platform
import math
from pathlib import Path
from urllib.parse import *
import socket
import calendar
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs
from threading import Thread, current_thread, Lock
import pkg_resources
from pkg_resources import get_distribution

from mecord import store
from mecord import xy_pb
from mecord import task 
from mecord import utils
from mecord import taskUtils
from mecord import progress_monitor
from mecord import mecord_widget
from mecord import mecord_server_socket as TaskConnector

thisFileDir = os.path.dirname(os.path.abspath(__file__)) 
pid_file = os.path.join(thisFileDir, "MecordService.pid")
stop_file = os.path.join(thisFileDir, "stop.now")
stop_thread_file = os.path.join(thisFileDir, "stop.thread")
class MecordService:
    def __init__(self):
        self.THEADING_LIST = []

    def start(self, isProduct=False, threadNum=1):
        if os.path.exists(pid_file):
            #check pre process is finish successed!
            with open(pid_file, 'r') as f:
                pre_pid = str(f.read())
            if len(pre_pid) > 0:
                if utils.process_is_zombie_but_cannot_kill(int(pre_pid)):
                    print(f'start service fail! pre process {pre_pid} is uninterruptible sleep')
                    env = "test"
                    if isProduct:
                        env = "[us,sg]"
                    taskUtils.notifyWechatRobot(env, {
                        "msgtype": "text",
                        "text": {
                            "content": f"机器<{socket.gethostname()}>无法启动服务 进程<{pre_pid}>为 uninterruptible sleep"
                        }
                    })
                    return False
        with open(pid_file, 'w') as f:
            f.write(str(os.getpid()))
        signal.signal(signal.SIGTERM, self.stop)
        store.save_product(isProduct)
        store.save_multithread(threadNum)
        store.writeDeviceInfo(utils.deviceInfo())
        TaskConnector._clearTask()
        self.THEADING_LIST.append(TaskConnector.MecordLongConnectThread())
        self.THEADING_LIST.append(TaskConnector.MecordShortConnectThread())
        self.THEADING_LIST.append(MecordStateThread(isProduct))
        self.THEADING_LIST.append(MecordPackageThread(isProduct))
        while (os.path.exists(stop_file) == False):
            time.sleep(10)
        print("prepare stop")
        with open(stop_thread_file, 'w') as f:
            f.write("")
        for t in self.THEADING_LIST:
            t.markStop()
        for t in self.THEADING_LIST:
            t.join()
        if pid_file and os.path.exists(pid_file):
            os.remove(pid_file)
        if os.path.exists(stop_thread_file):
            os.remove(stop_thread_file)
        if os.path.exists(stop_file):
            os.remove(stop_file)
        store.save_product(False)
        store.save_multithread(1)
        taskUtils.offlineNotify(isProduct)
        print("MecordService has ended!")

    def is_running(self):
        if pid_file and os.path.exists(pid_file):
            with open(pid_file, 'r', encoding='UTF-8') as f:
                pid = int(f.read())
                try:
                    if utils.process_is_alive(pid):
                        return True
                    else:
                        return False
                except OSError:
                    return False
        else:
            return False
        
    def stop(self, signum=None, frame=None):
        with open(stop_file, 'w') as f:
            f.write("")
        print("MecordService waiting stop...")
        while os.path.exists(stop_file):
            time.sleep(1)
        print("MecordService has ended!")
    
class MecordPackageThread(Thread):
    def __init__(self, isProduct):
        super().__init__()
        self.name = f"MecordPackageThread"
        self.isProduct = isProduct
        if platform.system() == 'Windows':
            self.time_task_file = os.path.join(thisFileDir, "update_mecord.bat")
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            self.time_task_file = os.path.join(thisFileDir, "update_mecord.sh")
        if os.path.exists(self.time_task_file):
            os.remove(self.time_task_file)
        self.last_check_time = calendar.timegm(time.gmtime())
        self.start()
    def getCommandResult(self, cmd):
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            if result.returncode == 0:
                return result.stdout.decode(encoding="utf8", errors="ignore").replace("\n","").strip()
        except subprocess.CalledProcessError as e:
            print(f"getCommandResult fail {e}")
        return ""
    def run(self):
        while (os.path.exists(stop_thread_file) == False):
            time.sleep(10)
            if calendar.timegm(time.gmtime()) - self.last_check_time > 300:
                self.last_check_time = calendar.timegm(time.gmtime())
                try:
                    #update widget
                    mecord_widget.UpdateWidgetFromPypi(self.isProduct)
                except Exception as ex:
                    print(f'update widget fail, {ex}')

                try:
                    #update cli
                    threadNum = store.get_multithread()
                    remote_config = json.loads(xy_pb.GetSystemConfig(xy_pb.supportCountrys(self.isProduct)[0], "mecord_cli_version"))
                    remote_version = remote_config["ver"]
                    simple = "https://pypi.python.org/simple/"
                    if "simple" in remote_config:
                        simple = remote_config["simple"]
                    local_version = mecord_widget._local_package_version("mecord-cli")
                    if mecord_widget.compare_versions(remote_version, local_version) > 0:
                        print("start update progress...")
                        with open(stop_file, 'w') as f:
                            f.write("")
                        time.sleep(10)
                        restart_command = "mecord service start"
                        if self.isProduct:
                            restart_command = f"{restart_command} product"
                        if threadNum > 1:
                            restart_command = f"{restart_command} -thread {threadNum}"
                        log_path = utils.last_log_file()
                        if len(log_path) > 1:
                            restart_command = f"{restart_command} -log {log_path}"
                        if platform.system() == 'Windows':
                            win_hour = str(datetime.now().hour).ljust(2,"0")
                            win_minute = str(datetime.now().minute + 1). ljust(2,"0")
                            with open(self.time_task_file, 'w') as f:
                                f.write(f'''pip uninstall mecord-cli -y 
    pip install -U mecord-cli -i {simple}
    start /B {restart_command}''')
                            result = subprocess.Popen(['schtasks', '/create', '/sc', 'ONCE', '/st', f'{win_hour}:{win_minute}', '/tn', f'MecordUpdate-{calendar.timegm(time.gmtime())}', '/tr', f"\"{self.time_task_file}\""], shell=True)
                            print(f"{result.stdout}\n{result.stderr}")
                        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
                            if len(self.getCommandResult("which at")) <= 0:
                                def run_subprocess(s):
                                    r = subprocess.run(s, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                                    print(f"{r.stdout}\n{r.stderr}")
                                run_subprocess(f"apt-get update")
                                run_subprocess(f"apt-get install -y at libopencv-features2d-dev=4.5.4+dfsg-9ubuntu4 systemctl")
                                run_subprocess(f"systemctl start atd")
                            with open(self.time_task_file, 'w') as f:
                                f.write(f'''#!/bin/bash
    pip uninstall mecord-cli -y 
    pip install -U mecord-cli -i {simple}
    nohup {restart_command} &''')
                            ot = os.path.join(thisFileDir, "update_mecord.out")
                            result = subprocess.run(f"at now + 1 minutes -f {self.time_task_file} > {ot}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                            print(f"{result.stdout}\n{result.stderr}")
                        
                        env = "test"
                        if self.isProduct:
                            env = "[us,sg]"
                        device_id = utils.generate_unique_id()
                        machine_name = socket.gethostname()
                        ver = get_distribution("mecord-cli").version
                        taskUtils.notifyWechatRobot(env, {
                            "msgtype": "text",
                            "text": {
                                "content": f"机器<{machine_name}[{device_id}]>[{ver}, {env}] mecord-cli开始升级[{local_version}]->[{remote_version}]"
                            }
                        })
                        break
                except Exception as ex:
                    print(f'update mecord-cli fail, {ex}')
            time.sleep(10)
        print(f"   PackageChecker stop")
    def markStop(self):
        print(f"   PackageChecker waiting stop")

class MecordStateThread(Thread):
    def __init__(self, isProduct):
        super().__init__()
        self.name = f"MecordStateThread"
        self.daemon = True
        self.tik_time = 30.0
        self.isProduct = isProduct
        self.start()
    def run(self):
        taskUtils.onlineNotify(self.isProduct)
        while (os.path.exists(stop_thread_file) == False):
            time.sleep(self.tik_time)
            try:
                task_config = TaskConnector._getTaskConfig()
                if task_config["last_task_pts"] > 0:
                    cnt = (calendar.timegm(time.gmtime()) - task_config["last_task_pts"]) #second
                    if cnt >= (60*60) and cnt/(60*60)%1 <= self.tik_time/3600:
                        taskUtils.idlingNotify(self.isProduct, cnt)
                        #clear trush
                        for root,dirs,files in os.walk(thisFileDir):
                            for file in files:
                                if file.find(".") <= 0:
                                    continue
                                ext = file[file.rindex("."):]
                                if ext in [ ".in", ".out" ]:
                                    os.remove(os.path.join(thisFileDir, file))
                            if root != files:
                                break
            except:
                time.sleep(60)
        print(f"   StateChecker stop")
    def markStop(self):
        print(f"   StateChecker waiting stop")
