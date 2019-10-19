import os
from config import setting

class GetLastReport(object):
    """获取最近一次测试报告"""
    def last_report_file(self):
        lists = os.listdir(setting.report_path)
        if not any(map(lambda t: t.endswith('html'),lists)):
            lists = ["html_report.html"]
        last_report_file = self.get_last_report_file(lists)
        # print(last_report_file)
        return last_report_file

    def get_last_report_file(self,lists):
        report_list = []
        for l_list in lists:
            if l_list.endswith('html'):
                report_list.append(l_list)

        last_report_file = report_list[-1]
        # print(report_list)
        return last_report_file

if __name__ == '__main__':
    get_last_report = GetLastReport()
    get_last_report.last_report_file()

