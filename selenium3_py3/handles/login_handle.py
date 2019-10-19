# coding=utf-8
from page_obj.login_page import LoginPage
from utils.loggers import Log
from utils import screenshot_file

logger = Log()


class LoginHandle(object):
    """打开页面后自动输入相应信息"""

    def __init__(self, driver):
        self.driver = driver
        self.login_p = LoginPage(self.driver)

    # 输入用户名
    def send_user_name(self, username):
        logger.file("输入的用户名是："+username)
        screenshot_file_path = screenshot_file()
        self.login_p.get_username_element().send_keys(username)
        logger.console("".format(screenshot_file_path))
        self.driver.save_screenshot(screenshot_file_path)

    # 输入密码
    def send_user_password(self, password):
        logger.file("输入的密码是："+password)
        self.login_p.get_password_element().send_keys(password)


    # 获取文字信息
    def get_login_error(self,info):
        try:  # 容错处理
            text_error = self.login_p.get_login_error_element()
        except:
            text_error = None
        return text_error

    # 点击登录按钮
    def click_submit_btn(self):
        self.login_p.get_submit_element().click()

    # 获取登录按钮文字
    def get_submit_btn_text(self):
        """如获取不到信息，表明页面已成功跳转"""
        return self.login_p.get_submit_element().text

    # 点击用户账号登录，转用户账号登录
    def click_login_qrcodebtn(self):
        return self.login_p.get_login_qrcodebtn_element().click()

