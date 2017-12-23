#coding=utf-8
'''
@author=chengww3
'''
import json,requests
from config.readConfig import ReadConfig
from common.logger import Log
class HTTPService:
    #def __init__(self):
        #rc = ReadConfig()
    #封装get方法
    def get(self,url,**dataset):
        params = dataset.get('params')
        headers = dataset.get('headers')
        lg = Log()
        try:
            resp = requests.get(url,params=params,headers=headers,timeout=5)
            text = resp.json()
            status_code = resp.status_code
            return text,status_code
        except Exception as e:
            lg.info(u'get请求错误：%s'%e)
    #封装post方法
    def post(self,url,**dataset):
        params = dataset.get('params')
        headers = dataset.get('headers')
        data = dataset.get('data')
        json = dataset.get('json')
        files = dataset.get('files')
        lg = Log()
        try:
            resp = requests.post(url,params=params,headers=headers,data=data,json=json,files=files,timeout=5)
            status_code = resp.status_code
            text = resp.json()
            return text,status_code
        except Exception as e:
            lg.info(u'post请求错误：%s'%e)

