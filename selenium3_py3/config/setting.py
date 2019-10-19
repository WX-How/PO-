import os

# 邮箱设置
receivers = ["1198699654@qq.com"]
sender = '13068029876@163.com'
email_host = "smtp.163.com"
email_user = "13068029876@163.com"    #设置自己的邮箱
email_pass = "*************"    #设置你自己的邮箱密码

# 日志级别设置
"""
级别排序:CRITICAL > ERROR > WARNING > INFO > DEBUG
debug
info
warning
error
critical


debug : 打印全部的日志,详细的信息,通常只出现在诊断问题上

info : 打印info,warning,error,critical级别的日志,确认一切按预期运行

warning : 打印warning,error,critical级别的日志,一个迹象表明,一些意想不到的事情发生了,或表明一些问题在不久的将来(例如。磁盘空间低”),这个软件还能按预期工作

error : 打印error,critical级别的日志,更严重的问题,软件没能执行一些功能

critical : 打印critical级别,一个严重的错误,这表明程序本身可能无法继续运行

"""

logger_level = "info"
logger_file = True
logger_console = True

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 项目首路径
logs_path = os.path.join(base_dir,'logs')  # 日志路径
config_ini = os.path.join(base_dir,'config','localElement.ini')  # localElement.ini 配置文件路径
report_path = os.path.join(base_dir,'report')  # report 配置文件路径
screenshot_path = os.path.join(base_dir,'report/screenshot')  # screenshot 截图路径