#coding=utf-8
'''
Created on 2017-7-10
@author: chengww3
Project:封装发送邮件功能:sendMail
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.logger import Log
import os

log = Log()
class SendMail:
    def sendMail(self,rootpath,sender,receiver,subject,username,password):
        #参数说明，发送者，接受者，邮件主题，发送者邮箱登录账号及密码

        # 发送邮箱服务器
        smtpserver = 'smtp.wps.cn'

        #定义测试报告目录

        reportdir =rootpath +"\\result\\report"
        files = os.listdir(reportdir)

        #按照时间对目录下的文件进行排序
        files.sort(key=lambda  fn:os.path.getmtime(reportdir+'\\'+fn))

        file = os.path.join(reportdir,files[-1])
        #print(file)
        #读取并获取文件内容
        f = open(file,'rb')
        content = f.read()
        f.close()

        #声明邮件是多模块
        msg = MIMEMultipart()
        #添加测试报告
        msg.attach(MIMEText(content,'html','utf-8'))
        msg['subject'] = Header(subject, 'utf-8')

        #构造附件
        #模块化log功能，生成log记录，获取最新的log文件
        #logdir = Getpath().getpath('log_path')
        logdir = rootpath + r"\result\log"
        logfiles = os.listdir(logdir)
        logfiles.sort(key=lambda fn:os.path.getmtime(logdir+'\\'+fn))
        logfile = os.path.join(logdir,logfiles[-1])
        #print(logfiles[-1])

        att = MIMEText(open(logfile).read(),'base64','utf-8')
        att['Content-Type'] = 'application/ocete-stream'
        att['Content-Disposition'] = 'attachment;filename='+logfiles[-1]
        msg.attach(att)

        try:
            smtp = smtplib.SMTP()
            #链接邮件服务器
            smtp.connect(smtpserver)
            #配置发送邮箱的用户名密码
            smtp.login(username,password)
            #配置发送邮箱，接收邮箱，以及发送内容
            smtp.sendmail(sender,receiver,msg.as_string())
            #关闭发邮件服务
            smtp.quit()
            log.info(u'发送邮件成功！')
        except Exception as  E:
            log.info(u'发送邮件失败!'+str(E))

