# coding=utf-8
from handles.login_handle import LoginHandle


class LoginBusiness(object):
    """测试注册页面form表单功能情况"""

    def __init__(self, driver):
        self.login_h = LoginHandle(driver)

    def user_base(self, username, password):
        self.login_h.click_login_qrcodebtn()  # 点击扫码登录，百度登录页面默认扫码登录，需点击并转到账号密码登录，才能进行下面的测试
        self.login_h.send_user_name(username)  # 定位并输入用户名
        self.login_h.send_user_password(password)  # 定位并输入密码
        self.login_h.click_submit_btn()  # 定位登录按钮，点击跳转

    def login_succes(self):
        if self.login_h.get_submit_btn_text() is None:
            # 登录成功
            return True
        else:
            return False

    # 数据驱动，只执行此条代码
    # 用户名、密码、错误提示信息
    def login_error_function(self, username, password):
        self.user_base(username, password)  # 输入账号、密码，点击登录后，查看是否有错误信息提醒
        if self.login_h.get_login_error('帐号或密码错误，请重新输入或者找回密码') is None:  # 没有错误信息，表示成功登录
            return True
        else:
            return False


