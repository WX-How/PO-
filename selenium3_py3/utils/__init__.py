# coding=utf-8

from config import setting
import datetime
import os

def screenshot_file():
    screenshot_path = setting.screenshot_path
    screenshot_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".png"
    return os.path.join(screenshot_path, screenshot_name)


