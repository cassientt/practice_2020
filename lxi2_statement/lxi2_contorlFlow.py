# if statements（条件循环语句）
# x = int(input("键盘输入一个整数: "))
# if x <0:
#     x == 0
#     print("如果输入是负数改变为零")
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# for Statements
# words = ['cat','windows','defenstrate']
# for  w in words:
#     print(w, len(w))

# for 循环复制一个列表之后再插入
# words = ['cat','window','defenstrate']
# for  w in words[:]:
#     if len(w) > 6:
#         words.insert(0,w)
#     # print(words) #打印每一次循环后给出的结果，有三个列表
# print(words)  #打印最终需要的结果

# 值：int, string, bool
# 引用：Object, Array

# 引用赋值
# arr = [1, 2, 3]
# copy = arr

# copy[0] = 100
# print(arr)
# print(copy)

# 值赋值
# str = 'hello'
# copy = str

# copy = 'hi'
# print(str)
# print(copy)

# 值赋值：数组（强制值赋值）
# arr = [1, 2, 3]
# copy = arr[:]

# copy[0] = 100
# print(arr)
# print(copy)

# range()
# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(2,10,3):
#     print(i)

# a = ['Mary','had','a','little','lamd']
# for i in range(len(a)):
#     print(i,a[i])

# enumerate(iterable,start=0) :枚举对象.Iterable要是iterator即支持迭代的对象。
# a = ['Mary','had','a','little','lamd']
# print(list(enumerate(a)))
# print(list(enumerate(a,start=2)))

# print(range(10))
# print(list(range(10)))


# print(list(range(2,2))) #空列表

# 没有返回结果
# for i in range(2,2):
#     print(i)

# break & continue,以及循环中的else子句
# break如果条件成立者接下来的所有循环均结束，打印本次对应条件下的结果

# for n in range(2,10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n,'equal',x,'*',n//x)
            # break 
# 如果条件成立执行条件下的打印，接下来的循环结束。如果条件不成立者执行else
#     else:
#         print(n,'is a prime number')

# continue（本次对应的结果不打印，继续接下来的循环迭代）
# for num in range(2,10):
#     if num % 2 ==0:
#         print('这是一个偶数even：',num)
#         continue
#     print('这是一个数字： ',num)

# Pass语句
while True:
    pass
class MyEmptyClass:
    pass
def initlog(*args)
    pass


# def fib(n):
#     """ 
#     """
