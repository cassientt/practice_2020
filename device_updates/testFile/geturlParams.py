import readConfig as readConfig

readConfig = readConfig.ReadConfig()

class geturlParams():
#定义一个方法，将从配置文件中读取的进行拼接
    def get_Url(self):
        new_url = readConfig.get_http('scheme') + '://' + readConfig.get_http('baseurl') + readConfig.get_http('parameter') + '?'
        return new_url

if __name__ == '__main__':
    print(geturlParams().get_Url())