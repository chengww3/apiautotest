#coding=utf-8
'''
Created on 2017/9/29
@author: chengww3
Project:执行接口自动化测试项目
'''

import os
from common.createSuite import CreateSuite
from common.createReport import CreatReport
from common.sendMail import SendMail
from config.readConfig import ReadConfig
def getRootPath():
    #获取根目录路径
    rootpath = os.path.dirname(os.path.realpath(__file__))
    return rootpath

if __name__ == '__main__':
    rootpath = getRootPath()
    testsuite = CreateSuite().creatSuite(rootpath)  # 获取测试套件
    # 搜索测试用例，执行测试，生成测试报告
    CreatReport().createReport(rootpath,u'接口自动化测试报告', u'test', testsuite)
    # 获取email的配置信息
    sender, receiver, subject, username, password = ReadConfig().getEmailConfig()
    SendMail().sendMail(rootpath,sender, receiver, subject, username, password)