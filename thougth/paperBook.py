# def hello():
#     print('你好，python！')
# hello()
# print( hello() )

# def hello(name='python'):
#     print('你好，%s!' % name)
# print('无参数调用时的输出')
# hello()
# print('有参数（“Json”）调用时的输出')
# hello('Json')

# def test(e = 3,a):
#     pass

# def change_para_num(*tpl):
#     print(type(tpl))
#     print(tpl)

# change_para_num(1)
# change_para_num(1,2,3)

# def change_para_dict(a, b = 0, **adct):
#     print('adct:', adct)
#     print('a:', a)
#     print('b:', b)
# change_para_dict(1, k = 3, b = 2, c = 3)

# def cube(name, **nature):
#     all_nature={'x':1,
#         'y':1,
#         'z':1,
#         'color':'white',
#         'weight':1}
#     all_nature.update(nature)
#     print(name,'立方体的属性：')
#     print('体积：',all_nature['x']*all_nature['y']*all_nature['z'])
#     print('颜色：',all_nature['color'])
#     print('重量：',all_nature['weight'])
# cube('first')
# cube('scond',y = 2,color = 'red')
# cube('scond',z = 2,weight = 10)

# def mysum(a, b):
#     return a+b

# print('拆解元组调用')
# print(mysum(*(3,4)))
# print('拆解字典调用')
# print(mysum(**{'a':3,'b':4}))



# L = list(filter(lambda x: x % 2 ==1, range(1, 20)))
# print(L)

# import math
# s = lambda x1, y1, x2, y2: math.sqrt((x1-x2)**2+(y1-y2)**2)
# print(s(1,1,0,0))

# alst=[0,1,2,3,4]
# print(list(filter(lambda x: x % 2,alst))) # [0, 2, 4, 6, 8]
# print(list(map(lambda x: 2*x,alst)))  #[0, 2, 4, 6, 8]
# print(isinstance('abc',str))  # True

# class MyClass:
#     pass
# print(MyClass)

# class MyClass:
#     "MyClass help."
# myclass = MyClass()
# print('输出类说明：')
# print(myclass.__doc__)
# print('显示类帮助信息：')
# help(myclass)

# class SmplClass:

#     def info(self):
#         print('我定义的类')

#     def mycalc(self, x, y):
#         return x + y

# sc = SmplClass()
# print('调用 info 方法的结果：')
# sc.info()
# print('调用 mycalc 方法的结果：')
# print(sc.mycalc(3, 4))

# class DemoInit:

#     def __init__(self, x, y = 0):
#         self.x = x
#         self.y = y

#     def mycalc(self):
#         return self.x + self.y

# dia = DemoInit(3)
# print('调用mycacl方法结果1: ')
# print(dia.mycalc())

# dia = DemoInit(3, 7)
# print('调用mycacl方法结果2: ')
# print(dia.mycalc())


# def coord_chng(x,y): # 定义全局函数，模拟坐标变换值，求绝对值
#     return (abs(x), abs(y))

# class Ant: #定义一个类

#     def __init__(self, x1 = 0, y1 = 0):  # 定义一个构造方法
#         self.x = x1
#         self.y = y1
#         self.disp_point() #构造函数中调用类中的方法

#     def move (self, x, y ):
#         x, y = coord_chng(x, y)
#         self.edit_point(x, y)
#         self.disp_point()

#     def edit_point(self, x2, y2):
#         self.x += x2
#         self.y += y2
    
#     def disp_point(self):
#         print("当前位置：（%d,%d)" %(self.x, self.y))
   
# ant_a = Ant()
# ant_a.move(2,4)
# ant_a.move(-9,6)


# class Demo_property:
#     class_name = "Demo_property" #类属性

#     def __init__(self, x1 = 0):
#         self.x = x1 #实例属性
#     def class_info(self):
#         print('类变量值： ',Demo_property.class_name)
#         print('实类变量值： ',self.x)
#     def chng(self,x2):  #修改实例属性的方法
#         self.x = x2
#     def chng_cn(self,name):   #修改类属性的方法
#         Demo_property.class_name = name

# dpa = Demo_property() #实例化dpa
# dpb = Demo_property()  #实例化dpb，两个对象dpa、dpb
# print("初始化两个实例")
# dpa.class_info()
# dpb.class_info()
# print("修改实例变量")
# print("修改dpa实例变量")
# dpa.chng(3)
# dpa.class_info()
# dpb.class_info()
# print("修改dpb实例变量")
# dpb.chng(10)
# dpa.class_info()
# dpb.class_info()
# print("修改类变量")
# print("修改dpa类变量")
# dpa.chng_cn('dpa')
# dpa.class_info()
# dpb.class_info()
# print("修改dpb实例变量")
# dpb.chng_cn('dpb')
# dpa.class_info()
# dpb.class_info()

# class DemoMthd:
#     @staticmethod
#     def static_mthd():
#         print("调用了静态方法")
#     @classmethod
#     def class_mthd(cls):
#         print("调用了类方法")
# DemoMthd.static_mthd()
# DemoMthd.class_mthd()
# dm = DemoMthd()
# dm.static_mthd()
# dm.class_mthd()


# class Ant:  # 定义类

#     def __init__(self, x1 = 0, y1 = 0, color1 = 'black'): #定义构造方法
#         self.x = x1
#         self.y = y1
#         self.color = color1
    
#     def crawl(self, x2 ,y2):
#         self.x = x2
#         self.y = y2
#         print('爬行')
#         self.info()
    
#     def info(self):
#         print('当前位置:(%d,%d)' %(self.x, self.y))
    
#     def attack(self):
#         print("用嘴咬")
# class FlyAnt(Ant):

#     def attack(self):
#         print("用尾针")
    
#     def fly(self, x3, y3):
#         print('飞行。。。。')
#         self.x = x3
#         self.y = y3
#         self.info()
# flyant = FlyAnt(color1='red')
# flyant.crawl(3, 5)
# flyant.fly(10, 14)
# flyant.attack()


# class PrntA:

#     namea = 'PrntA'
#     def set_value(self, a1):
#         self.a = a1
    
#     def set_namea(self,namea):
#         PrntA.namea = namea
    
#     def info(self):
#         print('PrntA:%s,%s' % (PrntA.namea,self.a))


# class PrntB:

#     nameb = 'PrntB'
    
#     def set_nameb(self,nameb):
#         PrntA.nameb = nameb
    
#     def info(self):
#         print('PrntB:%s' % (PrntB.nameb))

# class Sub(PrntA, PrntB):
#     pass
# class Sub2(PrntB,PrntA):
#     pass
# class Sub3(PrntA, PrntB):

#     def info(self):
#         PrntA.info(self)
#         PrntB.info(self)

# print('使用第一个子类：')
# sub = Sub()
# sub.set_value('aaa')
# sub.info()
# sub.set_nameb('BBB')
# sub.info()
# print('使用第二个子类：')
# sub2 = Sub2()
# sub2.set_value('aaa')
# sub2.info()
# sub2.set_nameb('BBB')
# sub2.info()
# print('使用第三个子类：')
# sub3 = Sub3()
# sub3.set_value('aaa')
# sub.info()
# sub3.set_nameb('BBB')
# sub3.info()


# x = 3
# class RefClass:
#     def __init__(self, v=5):
#         self.v =v

# class TestClass:
#     def __init__(self):
#         self.ref = RefClass()
#     def chng(self, x, y):
#         self.info()
#         x = 0
#         self.ref.v = 0
#         self.info()
#     def info(self):
#         print(x, self.v)
# tc = TestClass()
# tc.chng(0, 0)

# x = 3
# class RefClass:
#     def __init__(self, v=5):
#         self.v =v

# class TestClass:
#     def __init__(self):
#         self.ref = RefClass()
#     def chng(self, x, y):
#         self.info()
#         x = 0
#         self.ref.v = 0
#         self.info()
#     def info(self):
#         print(x, self.v)
# tc = TestClass()
# tc.chng(0, 0)

# str = "hello boy<[www.baidu.com]>byebye"

# str = str.split('[') # [ 'hello boy<', 'www.baidu.com]>byebyye' ]
# str = str[1] # 'www.baidu.com]>byebye'
# str = str.split(']') # [ 'www.baidu.com', '>byebye' ]
# str = str[0]

# print('str:', str)

# str = str.split('[')[1].split(']')[0]
# print('str:', str)


# import smtplib, email

# chst = email.charset.Charset(input_charset='utf-8')
# head = ("From: %s\n To:%s\n Subject:%s\n\n "
#         % ("cassientt@163.com",
#         "cassientt@163.com",
#         chst.header_encode("Python smtplib测试")))

# body = "你好！"
# email_con = head.encode('utf-8') + body.encode('utf-8')
# smtp = smtplib.SMTP("smtp.163.com")
# smtp.login("cassientt@163.com", "wm05251123")
# smtp.sendmail("cassientt@163.com", "cassientt@163.com", email_con)
# smtp.quit()


import threading

def thrfun(x, y):
    for i in range(x,y):
        print(str(i*i) + ';')
ta = threading.Thread(target=thrfun, args=(1,6))
tb = threading.Thread(target=thrfun, args=(16,21))
ta.start()
tb.start()


