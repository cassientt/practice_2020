import logging
class Test(object):
    def __init_(self,num):
        self.num = num
    def unnormal(self):
        try:
            print('开始测试异常情况')
            r = 10 /self.num
            print (r)
        except TypeError as e :
            print ( e )
        except ZeroDivisionError as e :
            logging.exception(e)
        finally:
            print(finally finish!)
op_test1=Test(num=2)
op_test1.unnormal()
op_test2=Test(num=Test)
op_test2.unnormal()
op_test3=Test(num=0)
op_test3.unnormal()
