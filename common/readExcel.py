#coding=utf-8
'''
Created on 2017/9/29
@author: chengww3
Project:读取表格文件
'''
import xlrd,os
from common.logger import Log
class ReadExcel(object):
    def __init__(self,rootpath,excelname,sheetName):

        excelpath = rootpath+"\\data\\"+excelname
        self.data = xlrd.open_workbook(excelpath)
        self.table = self.data.sheet_by_name(sheetName)
        
        self.row = self.table.row_values(0)
        self.col = self.table.col_values(0)
        
        self.rowNum = self.table.nrows
       
        self.colNum = self.table.ncols
       
        self.curRowNo = 1

    def analySheet(self):
        try:
            table = self.table#初始化确定sheet名称
            nrows = self.rowNum #总行数
            testcase = {}
            api_content = {}
            count = 1
            while count < nrows:
                rowdata = table.row_values(count)
                number = rowdata[0]

                api_content['describe'] = rowdata[1]
                api_content['verifyMethod'] = rowdata[2]
                api_content['requestMethod'] = rowdata[3]
                api_content['api'] = rowdata[4]
                api_content['headers'] = rowdata[5]
                api_content['body'] = rowdata[6]
                api_content['params'] = rowdata[7]
                api_content['hopeResult'] = rowdata[8]
                api_content['statusCode'] = rowdata[9]
                testcase[number] = api_content
                api_content = {}
                count = count + 1
            
            return testcase
        except:
            Log().info(u"api文件读取失败")
    #根据具体的用例编号获取响应的api内容
    def get_testcase_content(self,number):
        testcase = self.analySheet()

        return testcase.get(number)