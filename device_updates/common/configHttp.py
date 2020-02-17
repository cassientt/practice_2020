import requests
import json


class RunMain():
    def send_post(self, url, data):
        """ 
        定义一个方法，参数需要按照顺序传入url、data
        """
        result = requests.post(url = url, data = data).json() #需要封装post方法，所以url和data值不能写死
        res = json.dumps(result, ensure_ascii = False, sort_keys=True, indent=2)
        return res

    def send_get(self, url, data):
        result = requests.get(url = url, params = data).json()
        res = json.dumps(result, ensure_ascii =False, sort_keys=True, indent=2 )
        return res
    
    def run_main(self, method, url=None, data=None):  #定义此函数，通过传过来的method来进行不同get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data)
        elif method == 'get':
            result = self.send_get(url,data)
        else:
            print("method值错误！！！")
        return result
if __name__ == '__main__':
    result1=RunMain().run_main('post','https://crm-dev.imlaidian.com/terminal_upgrade_api//upgradePackage/analysis/v4', {'access_token':'tq2dnkx1i3nr4qhxB3outpobleyu4', 'packageName':'packageName', 'size':'5242880002'})
    print(result1)
