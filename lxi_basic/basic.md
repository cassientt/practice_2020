# Python Basic
### 闪光编程
终端敲入：` import this `  运行可以生成python之禅（模块就是一个别人写好了代码、功能齐全的Python文件。）   

### print（）函数告诉计算机把括号中的内容打印在计算机屏幕上。
### 在Python中，变量就像是一个带标签的“盒子”，需要你把数据放进去
‘变量命名要规范，赋值要用【=】表示，变量的最终值等于最后赋予的值’


括号中带单（双）引号：让计算机无需理解，原样复述引号中的内容。带三引号的：实现换行
函数在Python中指的是能实现某个具体功能的代码块。
运行代码出错可能原因有三种：  
Python的变量名使用了关键字，产生冲突；   
=是赋值操作符，==是比较操作符，这两种操作符用错；  
if条件判断、for和while循环、class和def声明，末尾没有添加英文冒号：  
解决思路  
根据可能的三种原因，排查错误。例如检查一下变量名是否跟关键字冲突。   
常见的Python3的关键字：and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None,, not, or, pass, raise, return, True, try, while, with




### print 方法的使用
```python
print('1024 * 768 =', 1024 * 768)  # 结果：100
print(4 * 3.75 -1) # 结果：100
```
There is full support for floating point; operators with 
mixed type operands convert the integer operand to floating 
point:
含有浮点数多运算会自动把全部数据转换为浮点数

### operators（运算符）
```python
print(17/3)
print(17 // 3)
print(17 % 3)
如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识
print('I\'m \"ok\"!')
```

* hello
* world


- hello
- world

1. hello
2. world

- [x] hello
- [ ] world


这是一段话，在话里嵌套代码这么些 `print('hello world')` 好的，你看到了。
