## 完整实例代码

# -*- coding: utf8
import requests
import hashlib
from datetime import　*
import json
# 登录获取cookie，作为全局变量
username = "13999999999"
password = hashlib.md5(b"123456").hexdigest()
url = "http://www.xxx.com/ajax/user_login/"
form_data = {"username":username,"password":password}
login_response = requests.post(url, data = form_data)
assert login_response.text == "success"
c = login_response.cookies


def make_order():
    # 定义方法选择餐厅及菜品
　　global c
　　url = "http://www.xxx.com/ajax/create_order/"
　　form_data = {"restaurant_id":11196, "menu_items_total":"12.00",
　　"menu_items_data":"[{'id':1653196,'p':'2','q':6 }]","delivery_fee":"3.00"}
　　make_response = requests.post(url, data = form_data,cookies = c)
　　res = make_response.text
　　id=json.loads(res)["order_id"] #由于返回的主体是JSON格式数据，需要将其转换成字典形式，并取出order_id对应的value值赋值给变量ID
　　assert id != "" #增加一个断言，ID获取成功必然不会为空，则继续执行后面的代码，如果ID为空，说明提交订单未成功，则终止后面的代码执行，并在运行结果报错。
　　return id


def place_order(id):# 并带上参数ID，把make_order()返回ID通过形式参数传递进来。
    # 定义方法下订单
　　global c
　　global username
　　time = datetime.now()+timedelta(hours=1)
　　url = "http://www.xxx.com/ajax/place_order/"
　　form_data = {"order_id":id,"customer_name":"xxxx",
　　"mobile_number":username,"delivery_address":"xxxxxxx",
　　"preorder":"yes", "preorder_time":time,"pay_type":"cash"}
　　place_response = requests.post(url,data = form_data,cookies = c)
　　res = place_response.text
　　assert res == "success"
　　print ("订餐成功")

""" 
完成了主要的订单流程之后，就可以开始解决短信验证码的问题了，为了代码的清晰和便于理解，
用一个函数来处理整个短信验证码模块，然后再通过判断结构嵌套每个具体功能函数。
"""
def sms():
result = ask_sms() #通过ask_sms()来获取是否需要用短信验证码，并将结果赋值给变量result。
if result == "{'status': 'ok','need_sms': False}":
　　return
# if判断当result的need_sms字段是False时，说明不需要短信验证码，则退出sms()函数并执行其他代码
else:
　　request_sms() # 则执行request_sms()请求发送短信到手机
　　code = get_sms() # 再通过get_sms()函数获取短信验证码并赋值给变量code
　　validate_sms(code) # 最后将code传入validate_sms()函数中发送验证请求。

def ask_sms():
    # 判断是否需要短信验证码
global c
global username
url = "http://www.xxx.com/ajax/is_order_need"
form_data = {"mobile":username}
ask_response = requests.post(url,data = form_data,cookies = c)
res = ask_response.text
　　　return res
# 返回是否需要发送短信验证码res的值。这里无法增加断言，因为返回的结果是不固定的，没法做判断。

def request_sms():
    # 处理请求发送验证码到手机的请求
　　global c
　　global username
　　url = "http://www.xxx.com/ajax/common_sms_code/"
　　form_data = {"mobile":username}
　　sms_response = requests.post(url,data = form_data,cookies = c)
　　res = sms_response.text
　　assert res == "True"
"""  
增加一个断言，如果返回代码的主体为True，则继续执行后面的代码，如果返回代码的主体不为True，
说明确定短信验证码未发送成功，则终止后面的代码执行，并在运行结果报错
"""

def get_sms():
    """ 
    接着再来处理获取短信验证码的请求，一般会有后台可以查询短信验证码，所以获取的方式就是登录后台，
    并通过接口查询指定手机号的短信验证码，这里把登录和获取短信放在一个函数里面，以方便cookie的传递。
    """
　　global username
　　url = "http://www.xxx.com/manager/login.action"
　　form_data = {"user":"admin","pwd":000000}
　　login_response = requests.post(url,data = form_data)
　　cookie =login_response.cookies
　　url2 = "http://www.xxx.com/manager/smsmanager"
　　form_data2 = {"phone":username}
　　code_response = requests.post(url2,data = form_data2,cookies = cookie)
　　code = code_response.text
　　assert code != ""
# 增加一个断言，如果查询的code不为空，则继续执行后面的代码；如果查询的code为空，说明未查到短信验证码，则终止后面的代码执行，并在运行结果报错。
　　return code

def validate_sms(code):
    # 得到了验证码之后就是验证功能的处理
　　global c
　　global username
　　url = "http://www.xxx.com/ajax/validate_sms_code/"
　　form = {"mobile":username,"sms_code":code}
　　validate_response = requests.post(url,data = form,cookies = c)
　　res = validate_response.text
　　assert code == "True"
if __name__ == "__main__":
　　id = make_order()
　　sms()
　　place_order(id)
