"""
@#!/usr/bin/env python
# -*- coding: utf-8 -*-
@author: ntt
@date  : 02/04/2020 18:20
@file  : 
"""
"""
快捷键注释：
shift+command+P：显示命令面板【在此处输入关键字查询快捷命令】
shift+option+A：多行注释
command+/：单行注释
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
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415926)
