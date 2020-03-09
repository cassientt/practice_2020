# a = 0
# b = 4
# print(a>b and a==b)
# print(a<b or a==b)
# print(not a!=b) 

# def add(a = 1,b = 2):
#     c = a + b
#     return a, b, c
# print(add())
# x, y, z  = add()
# print(x, y, z )

# import requests
# c = {"JSESSIONID":"43359E88FC2BDA774141CE4E840731D7"}
# # h = {"User-Agent":"Android/H60-L01/4.4.2/"}
# h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}
# test_url = "https://mail.163.com/js6/main.jsp?sid=XAtmXtQvMGinqkXRfXvvGARtYUvRofxo&df=mail163_mailmaster#module=welcome.WelcomeModule%7C%7B%7D"
# response=requests.get(test_url, cookies = c, headers = h)
# print (response.status_code)
# print (response.headers)
# print (response.text)


# import requests
# c = "JSESSIONID=43359E88FC2BDA774141CE4E840731D7"
# test_url = "https://mail.163.com/js6/main.jsp?sid=XAtmXtQvMGinqkXRfXvvGARtYUvRofxo&df=mail163_mailmaster#module=welcome.WelcomeModule%7C%7B%7D"
# response = requests.get(test_url ,headers={"cookie":c})
# print (response.status_code）
# print (response.headers）
# print (response.text)

# import requests
# h = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}
# c = {"JSESSIONID":"43359E88FC2BDA774141CE4E840731D7"}
# test_url = "https://mail.163.com/js6/main.jsp"
# p = {"sid": "XAtmXtQvMGinqkXRfXvvGARtYUvRofxo","df": "mail163_mailmaster#module=welcome.WelcomeModule%7C%7B%7D"}
# response = requests.get(test_url ,headers = h, cookies = c, params = p)
# print (response.status_code)
# print (response.headers)
# print (response.text)

# import requests
# test_url = "http://music.163.com/weapi/search/suggest/web?csrf_token="
# form = {"params":"BDqibj+HQR5hWEEPGxP6oD2T6wbbVWqQSMxemz7MHmMF2472SBpOqK/rQlpPry w2o4IZVSrK96yAA480wMbx7vX1eHi+Z+6iKzzTdaNsR1r4N9PGhAzYCBnJLmSu73Ih","encSecKey":"b39b6bef59f01a4072ec0314b45f0f1bfd263949cd64a10f0e9f104856c102 127deb2df53d8abe83ff5a23588771db03b2fea96833b8ee6c079216cbbc238835ccafa1e9bea39b912 697ca0bb4cd9044843545cb37c46f004114437ca1ec6b5c6dce4ba236cfaca2ed290ef6ca0f5319cc7e 388cc8c49b77a8c4c753e4c1102"}
# response = requests.post(test_url,data = form)
# print (response.status_code)
# print (response.headers)
# print (response.text)

# 1 import websocket
# 2 url = "ws://www.xxxx.com/xxxx"
# 3 ws = websocket.create_connection(url) # 创建链接
# 4 ws.send("{"request":1111,"service":1001,"name":"xxxx"}") # 通过send()方法发送请求的内容，即登录所需要的信息。
# 5 new_msg = ws.recv() #登录成功与否的返回信息
# 6 print (new_msg)
# 7 ws.send("{"request":"1111,"service":1003,"name":"x","message":"1111111"}")
# 8 new_msg1= ws.recv()
# 9 print (new_msg1)

# import unittest
# import requests

# class LoginTest(unittest.TestCase):
#     def setUp(self):
#         self.url = "http://www.xxx.com/login.html"
#     def test_login1(self):
#         form = {"username":13111111111,"password":123456}
#         r = requests.post(self.url,data = form)
#         self.assertEqual(r.text,"登录成功")
#     def test_login2(self):
#         form = {"username":"","password":123456}
#         r = requests.post(self.url,data = form)
#         self.assertEqual(r.text,"用户名不能为空")
#     def test_login3(self):
#         form = {"username":13111111111,"password":""}
#         r = requests.post(self.url,data = form)
#         self.assertEqual(r.text,"密码不能为空")
#     def test_login4(self):
#         form = {"username":13111111111,"password":111111}
#         r = requests.post(self.url,data = form)
#         self.assertEqual(r.text,"账号或者密码错误")

# import unittest
# import requests
# class LoginTest(unittest.TestCase):
# 　　　　省略之前的代码
#     def suite():
#         loginTestCase = unittest.makeSuite(logintest,"test")
#         return loginTestCase
# import random
# m = random.random()
# print(m)

# from datetime import *
# now = datetime.now()
# print (now)
# now_year = now.year
# now_month = now.month
# now_date = now.day
# now_weekday = now.isoweekday()
# print (now_year)
# print (now_month)
# print (now_date)
# print (now_weekday)

# from datetime import *
# now = date.today()
# tomorrow = now+timedelta(days=1)
# yesterday = now-timedelta(days=1)
# next_week = now+timedelta(days=7)
# print (now)
# print (tomorrow)
# print (yesterday)
# print (next_week)

# from datetime import *
# now = datetime.now()
# now_date = now.date()
# now_time = now.time()
# print (now)
# print (now_date)
# print (now_time)

# from datetime import *
# now = datetime.now()
# next_hour = now+timedelta(hours = 1)
# print (now)
# print (next_hour)

# import hashlib
# md5 = hashlib.md5(b"123456") # 通过hashlib下的md5()函数对密码进行加密
# password_md5 = md5.hexdigest() # 通过hexdigest()获取加密后的结果
# print (password_md5)

# import hashlib
# sha512 = hashlib.sha512(b"123456")
# password_sha512 = sha512.hexdigest()
# print (password_sha512)

# file = open("/Users/nietingting/lx/1.txt", "r")
# result = file.read()
# print (result)
# file.close()
""" 
abc,111,abc111
222,xyz,222xyz
"""

# file = open("/Users/nietingting/lx/1.txt", "r")
# result = file.readline()
# print (result)
# file.close()
# abc,111,abc111

# file = open("/Users/nietingting/lx/1.txt", "r")
# result = file.readlines()
# print (result)
# file.close()
# ['abc,111,abc111\n', '222,xyz,222xyz\n']

# file = open("/Users/nietingting/lx/1.txt", "r")
# result = file.readlines()
# for i in result:
#     print (i)
# file.close()
# """ 
# abc,111,abc111

# 222,xyz,222xyz
# """

# file = open("/Users/nietingting/lx/1.txt", "r")
# result = file.readlines()
# for i in result:
#     x = i.split(",",2)
#     print (type(x))
#     a = x[0]
#     b = x[1]
#     c = x[2]
#     print (a,b,c)
# file.close()
""" 
<class 'list'>
abc 111 abc111

<class 'list'>
222 xyz 222xyz
"""
file = open("/Users/nietingting/lx/1.txt", "a+")
file.write("xxx"+"\n")


file = open("/Users/nietingting/lx/1.txt", "w+")
file.write("YYY"+"\n")
file.write("ZZZ"+"\n")
