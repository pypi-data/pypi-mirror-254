import sys
import os
import argparse
import urllib3
import logging
import shutil
import datetime

sys.path.append('..')

from pkg_resources import parse_version
import platform
from mecord import utils
from mecord.capability_provider import CapabilityProvider
from mecord import xy_user

class LogStdout(object):
    def __init__(self):
        self.stdout = sys.stdout

    def write(self, message):
        if message != '\n':
            logging.info(message)
        self.stdout.write(message)

    def flush(self):
        self.stdout.flush()

    def __del__(self):
        self.close()

    def close(self):
        sys.stdout = self.stdout

def main():
    sys.stdout = LogStdout()
    utils.get_salt()
    urllib3.disable_warnings()


    idx = 2   
    logFilePath = f"{os.path.dirname(os.path.abspath(__file__))}/log.log"
    utils.save_log_file("")
    while idx < len(sys.argv):
        if sys.argv[idx] == "-log":
            logFilePath = sys.argv[idx+1]
            if os.path.isabs(logFilePath) == False:
                print(f"log path {logFilePath} is not avalid")
                sys.exit(0)
            utils.save_log_file(logFilePath)
        idx+=1

    if os.path.exists(logFilePath) and os.stat(logFilePath).st_size > (1024 * 1024 * 5) and ".log" in logFilePath:  # 5m bak file
        d = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        bakFile = logFilePath.replace(".log", f"_{d}.log")
        shutil.copyfile(logFilePath, bakFile)
        os.remove(logFilePath)

    if parse_version(platform.python_version()) >= parse_version("3.9.0"):
        logging.basicConfig(filename=logFilePath, 
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            encoding="utf-8",
                            level=logging.INFO)
    else:
        logging.basicConfig(filename=logFilePath, 
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            # encoding="utf-8",
                            level=logging.INFO)

    if len(sys.argv) >= 2:
        try:
            module = sys.argv[1]
            if len(module) != 0:
                CapabilityProvider().handle_action(module)
            else:
                print(f"Unknown command:{module}")
                utils.show_help()
                sys.exit(0)
        except Exception as e:
            print(f"uncatch Exception:{e}")
            return
        
    sys.stdout.close()

if __name__ == '__main__':
    main()
