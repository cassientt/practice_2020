# Python 常用的内建模块
## datetime
```python

from datetime import datetime
# 获取当前日期
time = datetime.now()
print(time) #2020-02-23 21:25:22.396179
print(type(time)) #<class 'datetime.datetime'>

# 获取指定日期和时间
dt = datetime(2020, 3, 1, 12, 20)
print(dt) #2020-03-01 12:20:00

# 把有时区概念的‘datetime’转换为有时区概念的‘timestamp’
dt1 = datetime(2018, 3, 1, 12, 20)
print(dt1.timestamp())  #2020-03-01 12:20:00
timestamp转换为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))  #2015-04-19 12:20:00

# str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)  #2015-06-01 18:19:59

# datetime转换为str
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S')) # 2020-02-23 22:06:24

""" 
datetime加减
对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
加减可以直接用+和-运算符，不过需要导入timedelta这个类：
"""
from datetime import datetime,timedelta
now = datetime.now()
print(now + timedelta(hours = 10)) 
#2015, 5, 18, 16, 57, 3, 540997
print(now - timedelta(days = 1, hours = 10)) 
#2020-02-22 12:16:21.020825

```


```python
from datetime import datetime, timedelta, timezone

# 获取当前datetime:
now = datetime.now()
print('now =', now)
print('type(now) =', type(now))

# 用指定日期时间创建datetime:
dt = datetime(2015, 4, 19, 12, 20)
print('dt =', dt)

# 把datetime转换为timestamp:
print('datetime -> timestamp:', dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print('timestamp -> datetime:', datetime.fromtimestamp(t))
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# 从str读取datetime:
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('strptime:', cday)

# 把datetime格式化输出:
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)

""" 
now = 2020-02-23 23:20:00.689384
type(now) = <class 'datetime.datetime'>
dt = 2015-04-19 12:20:00
datetime -> timestamp: 1429417200.0
timestamp -> datetime: 2015-04-19 12:20:00
timestamp -> datetime as UTC+0: 2015-04-19 04:20:00
strptime: 2015-06-01 18:19:59
strftime: Mon, Jun 01 18:19
current datetime = 2015-06-01 18:19:59
current + 10 hours = 2015-06-02 04:19:59
current - 1 day = 2015-05-31 18:19:59
current + 2.5 days = 2015-06-04 06:19:59
UTC+0:00 now = 2020-02-23 15:20:00.695269+00:00
UTC+8:00 now = 2020-02-23 23:20:00.695269+08:00
"""
```
## collection
* 集合模块，提供了很多有用的集合类（高性能容器的数据类型）
```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])

from collections import Counter
# 方法1
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# 方法2&3
from collections import Counter
c = Counter('programming')
print(c)

c = Counter()
c.update('programming')
print(c)

```
* 用 `namedtuple` 可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。【使用工厂方法创建带有命名的字段的元组的子类】
* `deque` 是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：【类似列表的容器，能够快速响应在任何一端进行pop】
* 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用 `defaultdict`【字典子类，调用一个工厂方法来提供缺失的值】
* `Counter` 是一个简单的计数器，例如，统计字符出现的个数：

# Base64
是一种用64个字符来表示任意二进制数据的方法
* 在一些项目中，接口的报文是通过base64加密传输的，所以在进行接口自动化时，需要对所传的参数进行base64编码，对拿到的响应报文进行解码；
```python
import base64

s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
print(str(s,'utf-8'))

d = base64.b64decode(s).decode('utf-8')
print(d)

s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
print(s)
d = base64.urlsafe_b64decode(s).decode('utf-8')
print(d)
```
# struct
Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
```python
import struct

bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

print(struct.unpack('<ccIIIIIIHH', bmp_header))
```
# 加密 
通过哈希算法，我们可以验证一段数据是否有效，方法就是对比该数据的哈希值，例如，判断用户口令是否正确，我们用保存在数据库中的password_md5对比计算md5(password)的结果，如果一致，用户输入的口令就是正确的。

* 如果salt是我们自己随机生成的，通常我们计算MD5时采用md5(message + salt)。但实际上，把salt看做一个“口令”，加salt的哈希就是：计算一段message的哈希时，根据不通口令计算出不同的哈希。要验证哈希值，必须同时提供正确的口令。

*  这实际上就是Hmac算法：Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中。

* 和我们自定义的加salt算法不同，Hmac算法针对所有哈希算法都通用，无论是MD5还是SHA-1。采用Hmac替代我们自己的salt算法，可以使程序算法更标准化，也更安全。
# hashlib
* 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。
```python
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())

```
# hmac
```python
import hmac
message = b'Hello, world!'
key = b'secret'
h = hmac.new(key, message, digestmod='MD5')
print(h.hexdigest())
```
* hmac输出的长度和原始哈希算法的长度一致。需要注意传入的key和message都是bytes类型，str类型需要首先编码为bytes。
# itertools
itertools模块提供的全部是处理迭代功能的函数，它们的返回值不是list，而是Iterator，只有用for循环迭代的时候才真正计算。


```python
import itertools

natuals = itertools.count(1)
for n in natuals:
    print(n)
    if n >= 100:
        break

cs = itertools.cycle('ABC')
t = 10
for c in cs:
    print(c)
    t = t - 1
    if t == 0:
        break
```
* 因为count(1)会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按 `Ctrl+C` 退出。
* cycle()会把传入的一个序列无限重复下去
* repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：

# contextlib
并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。
* 实现上下文管理是通过__enter__和__exit__这两个方法实现的

# python 常用的第三分模块
## Pillow
* 安装 `pip install pillow`
* 引用模块 `from PIL import Image, ImageDraw, ImageFont, ImageFilter
`
## requests
Python内置的urllib模块，用于访问网络资源。但是，它用起来比较麻烦，而且，缺少很多实用的高级功能。
* 更好的方案是使用requests。它是一个Python第三方库，处理URL资源特别方便。
* 安装： `pip install requests`

## chardet
使用chardet检测编码非常容易，chardet支持检测中文、日文、韩文等多种语言。

```python
import chardet
data = '离离原上草，一岁一枯荣'.encode('utf-8')
print(chardet.detect(data))
# {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
```
## psutil = process and system utilities(系统监控，跨平台使用)
 安装：`pip install psutil`
 ```python
 import psutil
# 获取cpu信息
# print(psutil.cpu_count())  #4 cup逻辑数量，4核非超线程
# print(psutil.cpu_count(logical=False)) #2  cup物理核心，2双核超线程
# 
# print(psutil.cpu_times()) # scputimes(user=31729.03, nice=0.0, system=22589.9, idle=443516.58)

# for x in range(5):
#     m = psutil.cpu_percent(interval=1,percpu=True)
#     print(m)
""" 
[16.0, 2.0, 13.0, 3.0]
[17.8, 3.0, 14.1, 2.0]
[16.2, 2.0, 16.0, 2.0]
[14.7, 3.0, 13.0, 3.0]
[13.1, 4.0, 15.0, 2.0]
"""
# 获取内存信息(物理内存和交换内存)
# wlmem=psutil.virtual_memory()
# print(wlmem)
# swapmem=psutil.swap_memory()
# print(swapmem)

# 获取磁盘信息
dis=psutil.disk_partitions
print(dis)
use = psutil.disk_usage('/')
print(use)
disio = psutil.disk_io_counters()
print(disio)
# 获取进程和网络信息
 ```
 * psutil还提供了一个test()函数，可以模拟出ps命令的效果：`psutil.test()`
 # virtualenv
 原理很简单，就是把系统Python复制一份到virtualenv的环境，用命令source venv/bin/activate进入一个virtualenv环境时，virtualenv会修改相关环境变量，让命令python和pip均指向当前的virtualenv环境