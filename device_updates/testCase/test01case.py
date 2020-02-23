import json
import unittest
from common.configHttp import RunMain
import urllib.parse
import readExcel
import geturlParams
import paramunittest
# 类似与ddt数据驱动

url = geturlParams.geturlParams().get_Url() #调用通过geturlParams获取我们拼接的URL。
sheet_xls = readExcel().get_xls('serverapkCase.xlsx','Sheet1')

@paramunittest.parametrized(*sheet_xls)
class testServerApk(unittest.TestCase):
    def setParameters(self, case_name, path,query,method):
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)

    def description (self):
        """ test report description """
        self.case_name
    
    def setUp(self):
        print(self.case_name+"测试开始前准备")
    
    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print('测试结束，输出log完成\n\n')

    def checkResult(self):
        """ check test result """

        url1 = "https://crm-dev.imlaidian.com/terminal_upgrade_api/"
        new_url = url1 + self.query
        data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        #将一个完整的URL中的para1=xx&para2=xx转换为{'para1':'xx','para2':'xx'}
        info = RunMain().run_main(self.method, url, data1)
        #根据Excel中的method调用run_main来进行requests请求，并拿到响应
        ss = json.loads(info)#将响应转换为字典
        if self.case_name == 'Server APK_error1':
            self.assertEqual(ss[result],201003)