import requests
import os
import json, time
from urllib.parse import *
from PIL import Image
from threading import Thread, current_thread, Lock

from mecord import xy_pb
from mecord import store
from mecord import taskUtils
from mecord import upload
from pathlib import Path 

class MecordAIGCTaskThread(Thread):
    params = False
    idx = 0
    call_back = None
    def __init__(self, idx, country, func, params, callback):
        super().__init__()
        self.idx = idx
        self.country = country
        self.func = func
        self.params = params
        self.call_back = callback
        if self.call_back == None:
            raise Exception("need callback function")
        self.start()
    def run(self):
        self.checking = False
        self.result = False, "Unknow"
        self.widgetid = xy_pb.findWidget(self.country, self.func)
        if self.widgetid > 0:
            checkUUID = xy_pb.createTask(self.country, self.widgetid, self.params)
            checking = True
            checkCount = 0
            while checking or checkCount > 600:
                finish, success, data = xy_pb.checkTask(self.country, checkUUID)
                if finish:
                    checking = False
                    if success:
                        self.call_back(self.idx, data)
                        return
                checkCount += 1
                time.sleep(1)
        else:
            print(f"widget {self.func} not found with {self.country}")
        self.call_back(self.idx, None)

class MecordAIGCTask:
    thread_data = {}

    def __init__(self, func: str, multi_params: list[dict], fromUUID=None):
        realTaskUUID = fromUUID
        country = "test"
        if store.is_multithread() or realTaskUUID != None:
            country = taskUtils.taskCountryWithUUID(realTaskUUID)
        else:
            firstTaskUUID, country = taskUtils.taskInfoWithFirstTask()
            if realTaskUUID == None:
                realTaskUUID = firstTaskUUID
        if country == None:
            country = "test"
            
        def _callback(idx, data):
            self.thread_data[str(idx)]["result"] = data
        idx = 0
        for param in multi_params:
            param["fromUUID"] = realTaskUUID
            self.thread_data[str(idx)] = {
                "thread" :  MecordAIGCTaskThread(idx, country, func, param, _callback),
                "result" : None
            }
            idx+=1
        
    def syncCall(self):
        for t in self.thread_data.keys():
            self.thread_data[t]["thread"].join()
        result = []
        for t in self.thread_data.keys():
            result.append(self.thread_data[t]["result"])
        return result
    
class TTSFunc(MecordAIGCTask):
    all_text = []
    def __init__(self, text: str = None, roles: list[dict] = [], fromUUID = None, multi_text: list[str] = []):
        if text != None:
            self.all_text = [text] + multi_text
        else:
            self.all_text = multi_text
        params = []
        for t in self.all_text:
            params.append({
                "mode": 0,
                "param":{
                    "messages": [
                        {
                            "content": t,
                            "roles": roles,
                        }
                    ],
                    "task_types": [
                        "generate_tts"
                    ]
                }
            })
        super().__init__("TaskTTS", params, fromUUID)

    def syncCall(self) -> tuple[float, str]:
        return self.singleSyncCall()
        
    def singleSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        try:
            tts_url = datas[0][0]["content"]["tts_results"][0]["tts_mp3"]
            tts_duration = datas[0][0]["content"]["tts_results"][0]["duration"]
            return tts_duration, tts_url
        except:
            return 0, None
        
    def multiSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        result = []
        try:
            idx = 0
            for t in self.all_text:
                if idx < len(datas):
                    tts_url = datas[idx][0]["content"]["tts_results"][0]["tts_mp3"]
                    tts_duration = datas[idx][0]["content"]["tts_results"][0]["duration"]
                    result.append({
                        "duration": tts_duration,
                        "url": tts_url,
                    })
                else:
                    result.append({
                        "duration": 0,
                        "url": "",
                    })
                idx += 1
        except:
            print("")
        return result
       
class Txt2ImgFunc(MecordAIGCTask):
    all_text = []
    def __init__(self, text: str = None, roles: list[dict] = [], fromUUID = None, multi_text: list[str] = []):
        if text != None:
            self.all_text = [text] + multi_text
        else:
            self.all_text = multi_text
        params = []
        for t in self.all_text:
            params.append({
                "mode": 0,
                "param":{
                    "messages": [
                        {
                            "content": t,
                            "content_summary": t,
                            "is_content_finish": True,
                            "message_type": "normal",
                            "roles": roles,
                        }
                    ],
                    "task_types": [
                        "generate_chapter_image"
                    ]
                }
            })
        super().__init__("TaskChapterImage", params, fromUUID)

    def syncCall(self) -> tuple[float, str]:
        return self.singleSyncCall()
        
    def singleSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        try:
            return datas[0][0]["content"]["chapter_image_urls"][0]
        except:
            return None
        
    def multiSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        result = []
        try:
            idx = 0
            for t in self.all_text:
                if idx < len(datas):
                    result.append({
                        "url": datas[idx][0]["content"]["chapter_image_urls"][0],
                    })
                else:
                    result.append({
                        "url": "",
                    })
                idx += 1
        except:
            print("")
        return result
     
class Audio2TextFunc(MecordAIGCTask):
    all_url = []
    def __init__(self, mp3Urls: list[str] = [], fromUUID = None):
        self.all_url = mp3Urls
        params = []
        for t in self.all_url:
            params.append({
                "mode": 0,
                "param":{
                    "model":"large",
                    "audio": t
                }
            })
        super().__init__("SpeechToText", params, fromUUID)

    def syncCall(self) -> tuple[float, str]:
        return self.singleSyncCall()
        
    def singleSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        try:
            return datas[0][0]["content"]["chapter_image_urls"][0]
        except:
            return None
        
    def multiSyncCall(self) -> tuple[float, str]:
        datas = super().syncCall()
        result = []
        try:
            idx = 0
            for t in self.all_url:
                if idx < len(datas):
                    result.append({
                        "text": datas[idx][0]["content"][0],
                        "lyric": datas[idx][0]["lyric"],
                        "language": datas[idx][0]["language"]
                    })
                else:
                    result.append({
                        "text": "",
                        "lyric": [],
                        "language": ""
                    })
                idx += 1
        except:
            print("")
        return result
    
     

            
# print(upload.upload("D:\\Program Files (x86)\\anaconda3\\Lib\\site-packages\\ttauto_crawler\\bin\\music\\091774eeb78fad8890d8eacd53145733.mp3", None))
# datas = Audio2TextFunc(mp3Urls=["http://yesdesktop-web-beta.oss-cn-shenzhen.aliyuncs.com/aigc/assets/2024/01/02/68a69440-e0dd-4954-af7a-aa991a78be3c.mp3"]).multiSyncCall()
# print(f"============= {datas}")

# import calendar
# aaa = calendar.timegm(time.gmtime())
# datas = Txt2ImgFunc(multi_text=[
#                     " test 2 test 2 test 2 test 2"], fromUUID="123123").multiSyncCall()
# print(f"============= {datas}")
# print(f"执行5个时间：{calendar.timegm(time.gmtime()) - aaa}")

# bbb = calendar.timegm(time.gmtime())
# tts_duration, tts_url = TTSFunc("啊哈哈哈哈，这是什么呀", []).syncCall()
# if tts_duration > 0:
#     print(f"tts成功。生成音频长度为{tts_duration}, 链接为{tts_url}")
# print(f"执行1个时间：{calendar.timegm(time.gmtime()) - bbb}")

# img_url = Txt2ImgFunc("啊哈哈哈哈，这是什么呀", []).syncCall()
# if img_url:
#     print(f"文生图成功   {img_url}")
