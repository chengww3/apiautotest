#coding=utf-8
'''
Created on 2017/9/29
@author: chengww3
Project:获取测试套件
'''
import unittest
class CreateSuite():
    # 获取所有的test case 添加到测试套件中
    def creatSuite(self,rootpath):
        testsuite = unittest.TestSuite()
        # 定义测试文件查找的目录

        test_dir = rootpath + "\\testCase"
        # 定义discover方法的参数
        discover = unittest.defaultTestLoader.discover(test_dir,
                                                       pattern='test*.py',
                                                       top_level_dir=None)

        # discover方法筛选出来的用例，循环添加到测试套件中

        for test_suite in discover:
            for test_case in test_suite:
                testsuite.addTests(test_case)
                # print (testsuite)
        return testsuite