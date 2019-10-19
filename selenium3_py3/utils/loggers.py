# coding:utf-8

import logging
import time
import os
from config import setting

# log_path是存放日志的路径

cur_path = os.path.dirname(os.path.realpath(__file__))

# log_path = os.path.join(os.path.dirname(cur_path),'logs')
log_path = setting.logs_path

#如果不存在这个logs文件夹，就自动创建一个

if not os.path.exists(log_path):
    os.mkdir(log_path)

class Log(object):
    def __init__(self):
        #文件的命名
        self.logname = os.path.join(log_path,'%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #日志输出格式
        self.formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        #日志级别
        self.level = setting.logger_level
        # 输入日志类型
        self.fh = None
        self.ch = None

    def __file(self, message):

        #创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(self.logname,'a',encoding='utf-8')#这个是python3的
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        self.__log_level(message)

        self.logger.removeHandler(fh)
        #关闭打开的文件
        # fh.close()
        # self.logger.hasHandlers()

    def __log_level(self, message):
        #区分日志级别
        if self.level =='info':
            self.logger.info(message)
        elif self.level =='debug':
            self.logger.debug(message)
        elif self.level =='warning':
            self.logger.warning(message)
        elif self.level =='error':
            self.logger.error(message)

    def __console(self, message):

        #创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        self.__log_level(message)

        #避免日志输出重复问题
        self.logger.removeHandler(ch)

    def __print(self, message):
        if setting.logger_file:
            self.__file(message)
        if setting.logger_console:
            self.__console(message)

    def file(self, message):
        self.__print(message)

    def console(self, message):
        self.__print(message)


if __name__ == "__main__":
    log = Log()
    log.console("sdfdsfsdfs")
    # log.file("sdfdsfsdfs")

