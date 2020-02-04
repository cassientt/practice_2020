"""
@#!/usr/bin/env python
# -*- coding: utf-8 -*-
@author: ntt
@date  : 02/04/2020 18:20
@file  : 
"""
# print('1024 * 768 =', 1024 * 768)
""" There is full support for floating point; operators with 
mixed type operands convert the integer operand to floating 
point:
含有浮点数多运算会自动把全部数据转换为浮点数
 """
# print(4 * 3.75 -1)
"""
 operators（运算符）:
/:division always returns a floating point number,To do floor division and get an integer result (discarding any fractional result) you can use the // operator; to calculate the remainder you can use %:
/：除法运算符，// ：除法运算取整数，%：除法运算符取余数 
"""
# print(17/3)
# print(17 // 3)
# print(17 % 3)
# 如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
# print('I\'m \"ok\"!')
# 字符串内部有很多换行，用\n(换行)写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容。\t：制表符
# print('''line1
# line2
# line3''')
""" 
变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头.
python是动态语言：即变量本身类型不固定当语言。
python中通常用大写的变量表示常量。
"""
# print('%2d-%02d' % (3,1))
# print('%.2f' % 3.1415926)
""" 
格式化：字符串中的有些字段是根据变量变化的，所以需要一种简便的格式化字符串的方式
在Python中，采用的格式化方式和C语言是一致的，用%实现
%%：表示一个%
%d：整数
%f:浮点数
%x：16进制整数
 """
print('growth rate: %d %%' % 7)
""" 
Python内置数据类型：
List[]：是一种有序的集合，可以随时添加和删除其中的元素。
list中元素类型可以不同，元素页可以是另外一个list
 可以通过len()函数可以获得list元素的个数
 使用索引访问list中每个元素的位置：list[len(classmates) - 1]=list[-1]
[负数的最后一位的整数会比正向取值多1，即为len()]
list中追加元素到末尾：classmates.append('Adam')
list中把元素插入到指定的位置：classmates.insert(1, 'Jack')
list中删除list列表中末尾的元素：classmates.pop()
list中删除list列表中指定位置：i的元素：classmates.pop(i)
list中指定的某个元素替换成为别的元素，可以直接赋值给对应的索引位置：classmates[1] = 'Sarah'
 """
 """ 
 另一种有序列表叫元组：tuple()，但tuple一旦初始化就不能修改【是说指向对象变化】
 因为tuple不可变，所以代码更安全
 tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
 只有1个元素的tuple定义时必须加一个逗号,来消除数学公式中的小括号
  """