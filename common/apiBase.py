#coding=utf-8
'''
Created on 2017/9/29
@author: chengww3
Project:api通用方法
'''

from common.logger import Log
from common.httpService import HTTPService
import os
class ApiBase(object):
    def get_response(self,url,method,**dataset):
        resp = None
        code = None
        if method == 'get':
            resp,code = HTTPService().get(url,**dataset)
        elif method == 'post':
            resp,code = HTTPService().post(url,**dataset)
        else:
            lg = Log()
            lg.info(u'暂不支持该请求方法')

        return resp,code
    def getRootPath(self):
        #获取的是该脚本文件的路径
        import re
        rootpath = os.path.dirname(os.path.realpath(__file__))
        strinfo = re.compile('common')
        rootpath2 = strinfo.sub('',rootpath)
        return rootpath2

# if __name__ == '__main__':
#     ab = ApiBase('account')
#     path = ab.getRootPath()
#     print(path)