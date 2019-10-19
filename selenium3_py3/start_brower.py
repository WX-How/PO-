#! -*- coding: utf-8 -*-

from selenium import webdriver

from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys
from  selenium.webdriver.support.ui import WebDriverWait
from  selenium.webdriver.support import  expected_conditions as EC

import  os
import  time
import  lxml.html
import  requests
from user_agent import generate_user_agent
from  utils.crawl import _crawl

def parse_doc(page_raw):
    '''
    :param page_raw:  html 源码
    :return: Element对象
    '''

    return lxml.html.fromstring(page_raw)

class ChromeDownloader(object):
    def __init__(self, proxy=None):
        # 设置代理
        self.proxy = proxy  # http://ip:port

    def __enter__(self):
        # 打开浏览器
        self.brower = self.get_browser()
        return self.brower

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭浏览器
        try:
            if self.brower:
                self.brower.quit()
        except Exception as e:
            print(e)

    def get_browser(self):
        co = webdriver.ChromeOptions()
        # co.add_argument('--headless')  # 无界面模式
        # co.add_argument('--disable-images') # 禁止加载图片，提高速度
        # co.add_argument('--disable-javascript')  # 禁用js
        # co.add_argument('--proxy-server=http://ip:port')  # 使用 代理

        # co.add_argument('--user-agent={}'.format(use))
        browser = webdriver.Chrome(
            chrome_options=co,
            executable_path='/usr/local/bin/chromedriver',
            service_log_path=os.path.devnull,
        )

        return  browser

def login_conpany(user_name, passwd):
    with ChromeDownloader() as browser:
        browser.get('https://weibo.com/')
        # print(browser.page_source) # 打印出html源码
        # 等待元素加载完成
        wait = WebDriverWait(browser, 20)

        et = wait.until(EC.presence_of_element_located((By.ID, "loginname")))
        et.send_keys(user_name)  # 填入你的微博账号

        et = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        et.send_keys(passwd)
        et.send_keys(Keys.RETURN)
        time.sleep(5)
        # et = browser.find_element_by_id("loginname")
        # et.send_keys(user_name)  # 填入你的微博账号
        #
        # et = browser.find_element_by_name("password")
        # et.send_keys(passwd)
        # et.send_keys(Keys.RETURN)

        cookies = browser.get_cookies()
        cookie = ';'.join([e['name'] + '=' + e['value'] for e in cookies])

    return  cookie


if __name__ == '__main__':
    cookie = login_conpany('liys_liys@163.com', '20ys')
    print(cookie)

    # 下面直接用requests 在header中加入cookie，即可完成登录，获取到页面数据
    headers = {'Cookie': cookie}

    page_raw = _crawl("get","https://weibo.com/2707072361/fans", headers=headers)
    print(page_raw)




