from config.setting import config_ini
import configparser

class Read_Ini(object):
    """读取配置文件信息"""
    def __init__(self,node = None):
        if node:
            self.node = node
        else:
            self.node = 'LoginElement'  # 配置文件中的某个节点
        self.cf = self.load_ini()

    def load_ini(self):  # 加载文件
        cf = configparser.ConfigParser()  # 使用 configparser模块读取配置文件信息
        cf.read(config_ini)  # 配置文件所在路径
        return cf

    def get_value(self,key): # 获取配置文件中key的value值
        data = self.cf.get(self.node,key)
        return data

# if __name__ == '__main__':
#     read_init = Read_Ini()
#     print(read_init.get_value('user_name'))

