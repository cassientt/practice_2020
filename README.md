# practice_2020

## basic_Python
### 1.基础
在Unix下 `contral+D`  exit the interprete，在window OS 下使用 `contral+z` 
or 使用 `quit()` 退出编辑器。

在python交互模式下只适合临时调试，不能保存代码，不适合在此模式下写代码。要选择一个可以适用的编辑器：比如VSCode、Pycharm等。
### 2.Number,string and operator
```python
print('1024 * 768 =', 1024 * 768) 
#结果：1024 * 768 = 786432
print(17/3) #5.666666666666667
print(17 // 3) #5
print(17 % 3) #2
```
/：除法运算符，// ：除法运算取整数，%：除法运算符取余数
含有浮点数多运算会自动把全部数据转换为浮点数

```python
print('I\'m \"ok\"!') #I'm "ok"!
```
如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识.字符串内部有很多换行，用\n(换行)写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容。\t：制表符.但有时为了代码风格好看会在triple引号中加入\来阻止因为敲来换行符而对于实际代码产生但换行                     
```python
print('%2d-%02d' % (3,1)) # 3-01
print('%.2f' % 3.1415926) #3.14
print('growth rate: %d %%' % 7) # growth rate: 7 %
```
变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头.                                                                  python是动态语言：即变量本身类型不固定当语言。
python中通常用大写的变量表示常量。

格式化：字符串中的有些字段是根据变量变化的，所以需要一种简便的格式化字符串的方式
在Python中，采用的格式化方式和C语言是一致的，用%实现。
%%：表示一个%    
%d：整数                                                                %f:浮点数  
%x：16进制整数

```python
print(3*'un' +'ium') 
#：unununium 字符串通过+拼接，通过*重复
print('py' 'thon') #python
#相邻但两个字符串会自动链接,但这种方法只适合链接字符串，变量或表达式并不适合。想要连接只能使用 +
```
### 字符串
字符串分隔与取索引:**索引越界会报错，切片中索引越界会自动处理**     
Python 中的字符串不能被修改，它们是 immutable 的。因此，向字符串的某个索引位置赋值会产生一个错误。如果想要改变可以新建通过+拼接
 ```python
word='python'
print(word[0]) #:p 角标从0开始
print(word[1:3])
#:yt 开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
print(word[:3])
#:pyt 省略开始索引时默认为0，省略结束索引时默认为到字符串的结束
print(word[4:]) 
#:on 默认到字符串长度结束，长度比实际多1，所以最后一个有包括
print(word[:2] +word[2:] ) #:python
print(word[-1]) #:n 从后向前
print(word[-4:]) #:thon 角标从0开始
print(word[-4:-2]) 
#:th  [a, b) print(word[:-2]) #:pyth  [a, b)
print(word[:-3] +word[-3:] ) #python
 ```

## 3.内置数据类型
Python内置数据类型：  
List[]：是一种有序的集合，可以随时添加和删除其中的元素、支持索引和切片。    
list中元素类型可以不同，元素页可以是另外一个list，但通常数据类型是相同的。    
可以通过built-in function len()函数可以获得list元素的个数  
使用索引访问list中每个元素的位置：list[len(classmates) - 1]=list[-1]  
[负数的最后一位的整数会比正向取值多1，即为len()]   
list中追加元素到末尾：classmates.append('Adam')  
list中把元素插入到指定的位置：classmates.insert(1, 'Jack')  
list中删除list列表中末尾的元素：classmates.pop()  
list中删除list列表中指定位置：i的元素：classmates.pop(i)  
list中指定的某个元素替换成为别的元素，lists are a mutable type ,可以直接赋值给对应的索引位置：classmates[1] = 'Sarah'
 
另一种有序列表叫元组：tuple()，但tuple一旦初始化就不能修改【是说指向对象变化】
因为tuple不可变，所以代码更安全  
tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
只有1个元素的tuple定义时必须加一个逗号,来消除数学公式中的小括号
"""
# 4.重要基础
## 4.1.0 print 函数介绍
### 条件语句：IF and input() functoin
```python
age = int(input('Input you age: '))
if age >= 18:
    print('Adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

```
注意:input()返回的是字符串，必须通过int()将字符串转换为整数，才能用于数值比较:

## 4.1.1 for 循环和 range()
```python
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)  #55

print(list(range(5)))  #[0, 1, 2, 3, 4]
```
Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来.  
range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
## 4.1.2 break and cotinue
```python
# break语法
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
# continue语法
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

break语句可以在循环过程中直接退出循环，而continue语句可以提前结束本轮循环，并直接开始下一轮循环。这两个语句通常都必须配合if语句使用。

要特别注意，不要滥用break和continue语句。break和continue会造成代码执行逻辑分叉过多，容易出错。大多数循环并不需要用到break和continue语句，上面的两个例子，都可以通过改写循环条件或者修改循环逻辑，去掉break和continue语句。

有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。
## 4.1.3 dict和set

```python
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1)) 
# 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除： 
s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
# s.remove/sort/add()
```
和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。而list相反：查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常要，需要牢记的第一条就是dict的key必须是不可变对象。和list比较，dict有以下几个特点：
查找和插入的速度极快，不会随着key的增加而变慢；需要占用大量的内存，内存浪费多。而list相反：

查找和插入的时间随着元素的增加而增加；占用空间小，浪费内存很少。所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

# 5 Function（函数）
### 5.1 调用函数
Python内置了很多有用的函数，我们可以直接调用。要调用一个函数，需要知道函数的名称和参数，比如求绝对值的函数abs，只有一个参数。可以直接从Python的官方网站查看文档：

http://docs.python.org/3/library/functions.html#abs

也可以在交互式命令行通过help(abs)查看abs函数的帮助信息。
例如：数据类型转换也是 python 内置函数的调用。

### 5.2 定义函数
在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

### 5.3 函数参数

### 必选参数&默认参数

为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


### 可变参数：
```python
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
```
允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
### 关键字参数：
```python
def person(name, age, **kw):
print(person('Bob', 35, city='Beijing'))
```
允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：