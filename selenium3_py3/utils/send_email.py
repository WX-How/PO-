import smtplib
from email.mime.text import MIMEText
from email.header import Header
from utils.get_last_report import GetLastReport
from config import setting
import os


last_report = GetLastReport()
report_file = last_report.last_report_file()

class SendEmail(object):
    def __init__(self,receivers = None):
        self.mail_host = setting.email_host  # 设置服务器
        self.mail_user = setting.email_user # 用户名
        self.mail_pass = setting.email_pass  # 密令/密码

        self.sender = setting.sender
        if setting.receivers:
            self.receivers = setting.receivers
        else:
            self.receivers = ['1198699654@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    def get_report_file(self,report_file):
        """获取最近一次测试报告"""
        report_path = os.path.join(setting.report_path,report_file)
        with open(report_path,'rb') as f:
        # f = open(report_path,'rb')
            mail_content = f.read()
        return mail_content

    def send_email(self,report_file):

        content = self.get_report_file(report_file)
        message = MIMEText(content, _subtype='html', _charset='utf-8')  # 邮件内容
        subject = '百度登录-自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')  # 邮件主题
        message['From'] = self.sender  # 发送人，必填，邮箱格式
        message['To'] = ";".join(self.receivers)  # 收件人，必填，邮箱格式

        server = smtplib.SMTP()
        server.connect(self.mail_host, 25)  # 连接服务器
        server.login(self.mail_user, self.mail_pass)  # 登录
        try:
            server.sendmail(self.sender, self.receivers, message.as_string())
            print('邮件发送成功')
        except smtplib.SMTPException as e:
            print("Error: 无法发送邮件")
        server.close()

if __name__ == "__main__":
    send_email = SendEmail()
    send_email.send_email(report_file)

