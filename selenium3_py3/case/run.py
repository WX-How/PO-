# coding=utf-8
import unittest
from case import first_ddt_case
import datetime
import  os
from config import setting
from utils.get_last_report import GetLastReport
from utils.send_email import SendEmail
from utils.loggers import Log
from utils.HTMLTestRunner import HTMLTestRunner

logger = Log()

def main():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    # loader.testMethodPrefix = 'ab'
    # suite.loadTestsFromTestCase(FirstDdtCase)
    test_cases = loader.loadTestsFromModule(first_ddt_case)
    suite.addTests(test_cases)

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
    logger.file(report_file)
    # send_email = SendEmail()  # 发送邮件
    # send_email.send_email(report_file)


if __name__=="__main__":
    main()