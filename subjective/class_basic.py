# class Student(object): #通过class关键字来定义类，class后面紧跟的是类名【通常类名首字母需要大写】
#     #‘object’表示该类是从那个类继承来的，如果没有合适的继承类就使用‘obgect’类，这是所有的类都会继承的类。
#     def __init__(self,name,score): #属性：静态数据
#         self.__name = name
#         self.score = score
#     def print_score(self): #方法：动态的处理函数
#         print('%s:%s'%(self.__name,self.score))

# pupil=Student(name='lili',score=99) #实例化类是在类名后面加（），类不可以被直接使用，只能先将其实例化，然后用实例代表类进而调用类中的方法处理数据
# pupil.print_score()
# 类的访问权限：在类的外部不可以直接调用类中的数据。
# 在python中，在变量前面加`__`可以将变量置为私有变量。使其只能在类中使用，不能被类之外的其它函数（方法）调用。

# 继承
class Parent(object):
    def print_self(self):
        return "我是父类"
# 子类继承父类[方法直接在类名称的括号中加上父类的名称]：继承
class Student(Parent):
    def __init__(self,name,score):
        self.__name = name
        self.score = score
    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))
MaiMai = Student('hello',99)
print(MaiMai.score)
# 直接在子类中使用父类的方法
print(MaiMai.print_self())


# 类的多态：即如果子类继承了父类，又想改变父类的方法，则无需修改父类，只需要在子类中添加相同的方法名，就可以起到覆盖的作用。
class Parent(object):
    def print_self(self):
        return "我是父类"
# 子类继承父类
class Student(Parent):
    def __init__(self,name,score):
        self.__name = name
        self.score = score
    def print_score(self):
        print('%s: %s' %(self.__name, self.__score))
    def print_self(self):
        return "我是子类"
MaiMai = Student('hello',99)
print(MaiMai.score)
# 直接在子类中使用父类的方法
print(MaiMai.print_self())

