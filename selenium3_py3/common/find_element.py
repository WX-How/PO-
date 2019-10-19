#coding=utf-8
from utils.read_ini import Read_Ini

class FindElement(object):
    """根据配置文件信息，获取元素所在位置"""
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = Read_Ini()
        data = read_ini.get_value(key)
        by,value = data.split('>')

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'css':
                return self.driver.find_elements_by_css_selector(value)[0]
            else:
                return self.driver.find_element_by_tag_name(value)
        except Exception as e:
            # print("find_element错误信息：",e)
            return None

