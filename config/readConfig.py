#coding=utf-8
'''
Created on 2017/9/29
@author: chengww3
Project:
'''
import yaml,os
from common.logger import Log
class ReadConfig(object):
    def __init__(self):
        self.rootpath = self.getRootPath()

    # 读取yaml文件
    def readYaml(self, yamlname):
        #rootPath = self.getRootPath()
        try:
            yamlPath = self.rootpath + '\\' + yamlname + '.yaml'
            self.file = open(yamlPath, encoding='UTF-8', errors='ignore')
            ml= yaml.load(self.file)
            return ml
        except IOError :
            Log().info(u"yaml文件读取失败")
        finally:
            self.file.close()

    def getRootPath(self):
        # 获取的是该脚本文件的路径
        import re
        rootpath = os.path.dirname(os.path.realpath(__file__))
        strinfo = re.compile('common')
        rootpath2 = strinfo.sub('config', rootpath)
        return rootpath2
    #获取邮件配置信息
    def getEmailConfig(self):
        pass

    #获取api基础配置信息，例如host，url等
    
	'''
	删除敏感get方法
	'''
	
    def get_origin(self,type):
        #type account或者drive
        ml = self.readYaml('baseConfig')
        origin = ml['Origin']
        return origin[type]
    def get_url(self,type):
        ml = self.readYaml('baseConfig')
        url =ml['url']
        return url[type]
    def get_account(self):
        ml = self.readYaml('baseConfig')
        account = ml['account']
        username = account['username']
        password = account['password']
        return username,password

if __name__ == '__main__':
    rc = ReadConfig()
    