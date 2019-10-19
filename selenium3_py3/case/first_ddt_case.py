# coding=utf-8

import ddt
import unittest
import os
from selenium import webdriver
from config import setting
from business.login_business import LoginBusiness
from utils.get_last_report import GetLastReport
from utils.send_email import SendEmail
from utils.loggers import Log
from utils.HTMLTestRunner import HTMLTestRunner
import datetime

# sys.path.append(setting_conf.base_dir)

loger = Log()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://passport.baidu.com/v2/?login') #访问百度用户登录界面
        self.driver.refresh()
        self.driver.maximize_window()
        self.login = LoginBusiness(self.driver)
        self.driver.implicitly_wait(5)

        # self.login = RegisterBusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:  # case如果执行失败，错误会保存到_outcome.errors 中
            if error:
                case_name = self._testMethodName  # case名，即定义好的方法名
                report_error_name = case_name + '.png'
                report_error_path = os.path.join(setting.report_path,'screenshot', report_error_name)
                self.driver.save_screenshot(report_error_path)
        # self.driver.close()
        self.driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()

    @ddt.data(('13068029876','**********'),('755318368','200800lys'))  #测试数据
    @ddt.unpack
    def test_login_case(self,username,pwd):   # ex_data:[[],[],..] 列表套列表
        login_error = self.login.login_error_function(username, pwd)
        self.assertFalse(login_error,"登录成功，测试失败！") # login_error如果不等于False，表示没有错误信息，登录成功。此条case测试失败


"""
def run():
    suite = unittest.TestLoader()
    # suite.loadTestsFromTestCase(FirstDdtCase)
    suite.loadTestsFromModule(FirstDdtCase)
    report_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".html"
    report_file = os.path.join(setting.report_path,report_name)
    with open(report_file, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            title="This is the first ddt_case report1",
            description="这个是我们第一次测试报告 --数据驱动",
            verbosity=2
        )
        runner.run(suite)

    last_report = GetLastReport()
    report_file = last_report.last_report_file()  # 获取最近一次报告
    loger.file(report_file)
    # send_email = SendEmail()  # 发送邮件
    # send_email.send_email(report_file)

"""
