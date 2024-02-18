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
import threading
import socket
import datetime
import calendar
from urllib.parse import urlparse, parse_qs
from threading import Thread, current_thread, Lock
import pkg_resources
from pkg_resources import get_distribution
import websocket
import uuid
import queue
from threading import Thread, current_thread, Lock

from mecord import store
from mecord import xy_pb
from mecord import task 
from mecord import constant 
from mecord import utils
from mecord import taskUtils
from mecord import progress_monitor
from mecord import mecord_widget
import mecord.pb.tarsproxy_pb2 as tarsproxy_pb2

thisFileDir = os.path.dirname(os.path.abspath(__file__))
class MecordLongConnectThread(Thread):
    url = "wss://mecord-beta.2tianxin.com/proxymsg/ws" 
    ws = None
    extend_config = {}
    token = xy_pb.real_token()
    device_id = utils.generate_unique_id()
    is_product = store.is_product()
    service_country = "test"
    THEADING_LIST = []
    max_counter = store.get_multithread()
    cur_counter = 0
    is_running = False
    heartbeat_thread = None
    task_queue = queue.Queue()
    ttt = 0
    
    def receive_unknow_func():
        pass
    def receive_GetTask(self, body):
        rsp = xy_pb.aigc_ext_pb2.GetTaskRes()
        rsp.ParseFromString(body)
        self.ttt = time.time() * 1000
        for it in rsp.list:
            self.cur_counter+=1
            self.task_queue.put([{
                "taskUUID": it.taskUUID,
                "pending_count": rsp.count - rsp.limit,
                "config": it.config,
                "data": it.data,
            }, rsp.timeout])
    def receive_TaskNotify(self, body):
        rsp = xy_pb.aigc_ext_pb2.TaskNotifyRes()
        rsp.ParseFromString(body)
        if rsp.ok and len(rsp.notify_id) > 0:
            xy_pb.resetLastTaskNotify(rsp.task_uuid)
            taskUtils.taskPrint(rsp.task_uuid, f"{current_thread().name}=== task : {rsp.task_uuid} notify server success")
        else:
            taskUtils.taskPrint(rsp.task_uuid, f"{current_thread().name}=== task : {rsp.task_uuid} server fail~~ rsp={rsp}")
    def receive_TaskInfo(self, body):
        rsp = xy_pb.aigc_ext_pb2.TaskInfoRes()
        rsp.ParseFromString(body)

    def on_message(self, ws, message):
        try:
            msg = tarsproxy_pb2.Message()
            msg.ParseFromString(message)
            cases = {
                "mecord.aigc.AigcExtObj_GetTask": self.receive_GetTask,
                "mecord.aigc.AigcExtObj_TaskNotify": self.receive_TaskNotify,
                "mecord.aigc.AigcExtObj_TaskInfo": self.receive_TaskInfo,
            }
            return cases.get(f"{msg.obj}_{msg.func}", self.receive_unknow_func)(msg.body)
        except Exception as ex:
            pass
    def on_error(self, ws, error):
        print(f"Connection on_error (error: {error})")
        if "Connection to remote host was lost" in str(error):
            print(f"close socket & sleep(5)")
            self.ws.close()
            time.sleep(3)
        if self.is_running:
            self.reconnect()
        pass
    def on_close(self, ws, status_code, close_msg):
        print(f"Connection closed (status code: {status_code}, message: {close_msg})")
        time.sleep(3)
        if self.is_running:
            self.reconnect()
    def reconnect(self):
        print(f"reconnect...")
        self.run_forever()
    def on_ping(self, ws, message):
        print(f"on_ping... {message}")
    def on_pong(self, ws, message):
        print(f"on_pong... {message}")
    def on_open(self, ws):
        self.GetTask()
    def run_forever(self):
        if self.ws:
            self.ws.run_forever(ping_interval=10, ping_timeout=5, ping_payload="mecord")

    def __init__(self):
        threading.Thread.__init__(self)
        self.name = "MecordLongConnectThread"
        extInfo = store.readDeviceInfo()
        extInfo["app_version"] = constant.app_version
        extInfo["app_bulld_number"] = constant.app_bulld_number
        extInfo["app_name"] = constant.app_name
        extInfo["dts"] = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
        extInfo["trace_id"] = ''.join(str(uuid.uuid4()).split('-'))
        extInfo["salt"] = utils.get_salt()
        self.extend_config = json.dumps(extInfo)
        self.service_country = "test"
        if self.is_product:
            self.service_country = "US"
        self.is_running = True
        self.ws = websocket.WebSocketApp(self.url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close,
                                    on_ping=self.on_ping,
                                    on_pong=self.on_pong,
                                    header={
                                        f'deviceid:{self.device_id}'
                                    })
        self.ws.on_open = self.on_open
        self.start()

    def send_byte(self, b):
        try:
            if self.ws:
                self.ws.send_bytes(b)
        except:
            pass

    def heartbeat(self):
        last_heart_pts = calendar.timegm(time.gmtime())
        last_check_service_work_status_pts = calendar.timegm(time.gmtime())
        while self.is_running:
            cur_pts = calendar.timegm(time.gmtime())
            # if cur_pts - last_heart_pts > 10:
            #     heartbeat_data = { "type": "heartbeat" }
            #     binary_data = json.dumps(heartbeat_data).encode()
            #     self.send_byte(binary_data)
            #     print(f"{current_thread().name}=== heartbeat")
            #     #Previous tasks may have failed due to network problems, so collect and resend
            #     xy_pb.retryLastTaskNotify()
            #     last_heart_pts = cur_pts
            if cur_pts - last_check_service_work_status_pts > 120 and self.cur_counter == 0:
                task_config = _getTaskConfig()
                if task_config["last_task_pts"] > 0:
                    if calendar.timegm(time.gmtime()) - task_config["last_task_pts"] > 60:
                        #request once this device status
                        self.GetTask()
                        print(f"{current_thread().name}=== trigger timeout getTask!")
                last_check_service_work_status_pts = cur_pts
            time.sleep(5)
        print(f"   heartbeat stop")

    def taskRunning(self):
        service_country = "test"
        if self.is_product:
            service_country = "US"
        while self.is_running:
            try:
                data, timeout= self.task_queue.get()
                if data is None:
                    break
                try:
                    taskUUID = data["taskUUID"]
                    taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== receive {service_country} task : {taskUUID}")
                    _appendTask(taskUUID, service_country)
                    is_ok, msg, result = task.runTask(data, 60*60, self.is_product)
                    self.TaskNotify(taskUUID, is_ok, msg, result)
                    if is_ok == False:
                        taskUtils.notifyTaskFail(taskUUID, service_country, msg)
                    _removeTask(taskUUID)
                except Exception as e:
                    taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== task exception : {e}")
                    taskUtils.notifyScriptError(taskUUID, service_country)
                finally:
                    taskUtils.taskPrint(taskUUID, None)
                self.task_queue.task_done()
            except Exception as ex:
                taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== exception : {e}")
                pass
        print(f"   taskRunning stop")

    def _pb_pack(self, func, req):
        opt = {
            "lang": "zh-Hans",
            "region": "CN",
            "appid": "80",
            "application": "mecord",
            "version": "1.0",
            "X-Token": self.token,
            "uid": "1",
        }
        input_req = xy_pb.rpcinput_pb2.RPCInput(obj="mecord.aigc.AigcExtObj", func=func, req=req.SerializeToString(), opt=opt)
        return input_req.SerializeToString()
    def GetTask(self):
        req = xy_pb.aigc_ext_pb2.GetTaskReq()
        req.version = xy_pb.constant.app_version
        req.DeviceKey = self.device_id
        map = store.widgetMap()
        for it in map:
            if isinstance(map[it], (dict)):
                if map[it]["isBlock"] == False:
                    req.widgets.append(it)
            else:
                req.widgets.append(it)
        req.token = self.token
        req.limit = self.max_counter - self.cur_counter
        req.extend = self.extend_config
        req.apply = True
        print(f"{current_thread().name} waiting next {req.limit} task")
        self.send_byte(self._pb_pack("GetTask", req))
    def TaskInfo(self, taskUUID):
        req = xy_pb.aigc_ext_pb2.TaskInfoReq()
        req.taskUUID = taskUUID
        req.findTaskResult = True
        self.send_byte(self._pb_pack("TaskInfo", req))
    def TaskNotify(self, taskUUID, status, msg, dataStr):
        req = xy_pb.aigc_ext_pb2.TaskNotifyReq()
        req.version = constant.app_version
        req.taskUUID = taskUUID
        if status:
            req.taskStatus = xy_pb.common_ext_pb2.TaskStatus.TS_Success
        else:
            req.taskStatus = xy_pb.common_ext_pb2.TaskStatus.TS_Failure
        req.failReason = msg
        req.data = dataStr
        req.extend = self.extend_config
        xy_pb.saveTaskNotifyData(self.service_country, taskUUID, status, msg, dataStr)
        taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== notify {self.service_country} task : {taskUUID}")
        self.send_byte(self._pb_pack("TaskNotify", req))
        self.cur_counter-=1
        self.GetTask()

    def run(self):
        if self.ws:
            self.ws.close()
        if self.is_running:
            self.THEADING_LIST.append(Thread(target=self.heartbeat))
            for _ in range(0, self.max_counter):
                self.THEADING_LIST.append(Thread(target=self.taskRunning))
            for t in self.THEADING_LIST:
                t.start()
            self.run_forever()

    def markStop(self):
        self.is_running = False
        print(f"   MecordLongConnectThread waiting stop")
        if self.ws:
            self.ws.close()
            self.ws = None
        for _ in range(self.max_counter*2):
            self.task_queue.put([None, -1])
        for t in self.THEADING_LIST:
            t.join()
        print(f"   MecordLongConnectThread stop")

lock = Lock()
task_config_file = os.path.join(thisFileDir, f"task_config.txt")
def _readTaskConfig():
    if os.path.exists(task_config_file) == False:
        with open(task_config_file, 'w') as f:
            json.dump({
                "last_task_pts": 0
            }, f)
    with open(task_config_file, 'r') as f:
        data = json.load(f)
    return data
def _saveTaskConfig(data):
    with open(task_config_file, 'w') as f:
        json.dump(data, f)
def _appendTask(taskUUID, country):
    lock.acquire()
    task_config = _readTaskConfig()
    task_config[taskUUID] = {
        "country": country,
        "pts": calendar.timegm(time.gmtime())
    }
    task_config["last_task_pts"] = task_config[taskUUID]["pts"]
    _saveTaskConfig(task_config)
    lock.release() 
def _clearTask():
    lock.acquire()
    task_config = {
        "last_task_pts": 0
    }
    _saveTaskConfig(task_config)
    lock.release() 
def _removeTask(taskUUID):
    lock.acquire()
    task_config = _readTaskConfig()
    if taskUUID in task_config:
        del task_config[taskUUID]
    _saveTaskConfig(task_config)
    lock.release() 
def _taskCreateTime(taskUUID):
    pts = 0
    lock.acquire()
    task_config = _readTaskConfig()
    if taskUUID in task_config:
        pts = task_config[taskUUID]["pts"]
    lock.release()
    return pts 
def _getTaskConfig():
    lock.acquire()
    task_config = _readTaskConfig()
    lock.release() 
    return task_config

class MecordShortConnectThread(Thread):
    is_running = False

    def __init__(self):
        super().__init__()
        self.name = f"MecordShortConnectThread"
        self.is_running = True
        self.start()

    def run(self):
        is_product = store.is_product()
        what_time = 10
        supportCountrys = []
        if is_product:
            supportCountrys = ["SG"]
            what_time = 1
        while (self.is_running):
            for service_country in supportCountrys:
                taskUUID = ""
                try:
                    datas, timeout = xy_pb.GetTask(service_country)
                    for it in datas:
                        taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== receive {service_country} task : {taskUUID}")
                        _appendTask(taskUUID, service_country)
                        is_ok, msg, result = task.runTask(it, timeout, is_product)
                        xy_pb.TaskNotify(service_country, taskUUID, is_ok, msg, result)
                        if is_ok == False:
                            taskUtils.notifyTaskFail(taskUUID, service_country, msg)
                        _removeTask(taskUUID)
                except Exception as e:
                    taskUtils.taskPrint(taskUUID, f"{current_thread().name}=== {service_country} task exception : {e}")
                    taskUtils.notifyScriptError(taskUUID, service_country)
                finally:
                    taskUtils.taskPrint(taskUUID, None)
            time.sleep(what_time)
        print(f"   MecordShortConnectThread stop")

    def markStop(self):
        print(f"   MecordShortConnectThread waiting stop")
        self.is_running = False