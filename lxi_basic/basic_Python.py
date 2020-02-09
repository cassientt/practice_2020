"""
@#!/usr/bin/env python
# -*- coding: utf-8 -*-
@author: ntt
@date  : 02/04/2020 18:20
@file  : 
"""
# 字符串拼接方法
# print('The quick brown fox', 'jumps over', 'the lazy dog')
# print('growth rate: %d %%' % 7)
# print('1024 * 768 =', 1024 * 768)
# 运算
# print(4 * 3.75 -1)
# print(17/3)
# print(17 // 3)
# print(17 % 3)
# 转义字符
# print('I\'m \"ok\"!')
# 打印格式
# print('''\
# line1
# line2
# line3\
# ''')

# print('%2d-%02d' % (3,1))
# print('%.2f' % 3.1415926)

# print('C:\some\name')
# print(r'C:\some\name')  #通过在双引号之外加r来获取原始字符串
# print(3*'un' +'ium') #字符串通过+拼接，通过*重复
# print('py' 'thon')  #相邻但两个字符串会自动链接
# 字符串分隔与取索引
# word='python'
# print(word[0]) #:p 角标从0开始
# print(word[1:3]) #:yt 开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
# print(word[:3]) #:pyt 省略开始索引时默认为0，省略结束索引时默认为到字符串的结束
# print(word[4:]) #:on 默认到字符串长度结束，长度比实际多1，所以最后一个有包括
# print(word[:2] +word[2:] ) #:python
# print(word[-1]) #:n 从后向前
# print(word[-4:]) #:thon 角标从0开始
# print(word[-4:-2]) #:th  [a, b)
# print(word[:-2]) #:pyth  [a, b)
# print(word[:-3] +word[-3:] ) #python

# s = 'Python-中文'
# print(s)
# b = s.encode('utf-8')
# print(b)
# print(b.decode('utf-8'))

# Python内置数据类型：【list and tuple】
# squares = [1,4,9,16,25]
# print (len(squares)) #5
# print (squares[0]) #1
# print (squares[-1]) #25
# print (squares[-3:]) #[9, 16, 25]
# print (squares[:]) #[9, 16, 25]
# print(squares + [55,67,5]) #[1, 4, 9, 16, 25, 55, 67, 5]
# print(squares.append(7**2)) 

# The first one:fibonacci sepuence
# a,b = 0,1
# while a < 1000:
#     print(a,end="\n")
#     a,b = b,a+b

# input（）function and IF
# age = int(input('Input you age: '))
# if age >= 18:
#     print('Adult')
# elif age >= 6:
#     print('teenager')
# else:
#     print('kid')

# # for 循环和 range()
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)

# print(list(range(5)))

# print与for循环结合
# L = ['Bart', 'Lisa', 'Adam']
# for i in L:
#     print('hello, ', i)

# break语法
# n = 1
# while n <= 100:
#     if n > 10: # 当n = 11时，条件满足，执行break语句
#         break # break语句会结束当前循环
#     print(n)
#     n = n + 1
# print('END')

# continue语法
# n = 0
# while n < 10:
#     n = n + 1
#     if n % 2 == 0: # 如果n是偶数，执行continue语句
#         continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
#     print(n)

# d = {
#     'Michael': 95,
#     'Bob': 75,
#     'Tracy': 85
# }
# print('d[\'Michael\'] =', d['Michael'])
# print('d[\'Bob\'] =', d['Bob'])
# print('d[\'Tracy\'] =', d['Tracy'])
# print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1)) 
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除： 
# s1 = set([1, 1, 2, 2, 3, 3])
# print(s1)
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
# 调用函数
# x = abs(100)
# y = abs(-20)
# print(x, y)
# print('max(1, 2, 3) =', max(1, 2, 3))
# print('min(1, 2, 3) =', min(1, 2, 3))
# print('sum([1, 2, 3]) =', sum([1, 2, 3]))

# 切片
# L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# print('L[0:3] =', L[0:3])
# print('L[:3] =', L[:3])
# print('L[1:3] =', L[1:3])
# print('L[-2:] =', L[-2:])

# R = list(range(100))
# print('R[:10] =', R[:10])
# print('R[-10:] =', R[-10:])
# print('R[10:20] =', R[10:20])
# print('R[:10:2] =', R[:10:2])
# print('R[::5] =', R[::5])
# 高阶函数
def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))