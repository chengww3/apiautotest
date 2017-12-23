##接口自动化二次开发方案

开发环境：
>python3.6+requests+unittest
>测试报告模板使用的二次开发的HttpTestRunner.py

common目录：
>封装logger模块、获取测试套件、生成测试报告、发送邮件，读取表格

config目录：
>基本配置文件：yaml存储cookie等信息
>email配置文件：发送邮件的信息也在这里进行配置
>读取配置文件信息

data目录：
>存放api数据表格

result目录：
>存放log日志和测试报告

testCase目录：
>存放测试用例

run_all.py 开启测试

##目录结构

![这里写图片描述](http://img.blog.csdn.net/20171223205918153?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMTQ5MDgwMjc=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)