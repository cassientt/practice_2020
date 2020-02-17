import os
import configparser
import getpathInfo # 引用我们自己写的获取路径的类

path = getpathInfo.get_Path() #调用实例化，路径：/Users/nietingting/Developer/python/practice_2020/device_updates/testFile
config_path = os.path.join(path,'config.ini')#在path路径下再加一级。
config = configparser.ConfigParser()#调用外部的读取配置文件的方法
config.read(config_path,encoding='utf-8')

class ReadConfig():

    def get_http(self,name):
        value = config.get('HTTP',name)
        return value
    def get_email(self, name):
        value = config.get('EMAIL',name)
        return value
    def get_mysql(self,name):
        value = config.get('DATABASE',name)
        return value

if __name__ == '__main__':
    print('HTTP中的baseurl值为： ',ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：  ',ReadConfig().get_email('on_off'))

