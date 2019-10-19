from common.find_element import FindElement


class LoginPage(object):
    """操作 -->获取元素所在位置"""

    def __init__(self, driver):
        self.fd = FindElement(driver)

    # 获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("user_name")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")

    # 获取登录按钮元素
    def get_submit_element(self):
        return self.fd.get_element("login_submit")

    # 获取登录错误元素
    def get_login_error_element(self):
        return self.fd.get_element("login_error")

    def get_login_qrcodebtn_element(self):
        return self.fd.get_element("login_loginbtn")

