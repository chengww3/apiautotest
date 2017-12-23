#coding=utf-8
'''
Created on 2017-7-10
@author: chengww3
Project:封装生成测试报告函数createReport
'''
import time
import HTMLTestRunner
from common.logger import Log

class CreatReport:
    def createReport(self,rootpath,reportTitle,environment,testsuite):
        #参数说明：报告标题，测试环境，测试人员以及测试套件
        filetime = time.strftime("%Y_%m_%d %H_%M_%S")
        # 定义测试报告的存放路径
        #rootpath = Public().getRootPath()
        report_path = rootpath+"\\result\\report\\"

        filename = report_path + filetime + '_report.html'
        try:
            fp = open(filename, 'wb')

            # 定义测试报告标题，测试人员等信息
            runner = HTMLTestRunner.HTMLTestRunner(
                stream=fp,
                title=reportTitle,
                environment=environment,
            )
            runner.run(testsuite)
            # 关闭报告文件

            fp.close()
        except Exception as e:
            Log().info(e)
