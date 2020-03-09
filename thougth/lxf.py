from datetime import datetime
# # 获取当前日期
# time = datetime.now()
# print(time) #2020-02-23 21:25:22.396179
# print(type(time)) #<class 'datetime.datetime'>

# # 获取指定日期和时间
# dt = datetime(2020, 3, 1, 12, 20)
# print(dt) #2020-03-01 12:20:00

# 把有时区概念的‘datetime’转换为有时区概念的‘timestamp’
# dt1 = datetime(2018, 3, 1, 12, 20)
# print(dt1.timestamp())  #2020-03-01 12:20:00
# timestamp转换为datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))  #2015-04-19 12:20:00

# # str转换为datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)  #2015-06-01 18:19:59

# datetime转换为str
# now = datetime.now()
# print(now.strftime('%Y-%m-%d %H:%M:%S')) # 2020-02-23 22:06:24

# """ 
# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。
# 加减可以直接用+和-运算符，不过需要导入timedelta这个类：
# """
# from datetime import datetime,timedelta
# now = datetime.now()
# print(now + timedelta(hours = 10)) #2015, 5, 18, 16, 57, 3, 540997
# print(now - timedelta(days = 1, hours = 10)) #2020-02-22 12:16:21.020825

# 设置时区(搞不懂)
# from datetime import datetime, timedelta, timezone

# now = datetime.now()
# print(now)


# tz_utc_8 = timezone(timedelta(hours=1)) # 创建时区UTC+8:00

# dat1 = now.replace(tzinfo=tz_utc_8)
# print(dat1)  #2020-02-23 22:45:53.766963+08:00
# dat2 = now.replace(tzinfo=tz_utc_8)
# print(dat2)
# 时区转换
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)


# from datetime import datetime, timedelta, timezone

# # 获取当前datetime:
# now = datetime.now()
# print('now =', now)
# print('type(now) =', type(now))

# # 用指定日期时间创建datetime:
# dt = datetime(2015, 4, 19, 12, 20)
# print('dt =', dt)

# # 把datetime转换为timestamp:
# print('datetime -> timestamp:', dt.timestamp())

# # 把timestamp转换为datetime:
# t = dt.timestamp()
# print('timestamp -> datetime:', datetime.fromtimestamp(t))
# print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(t))

# # 从str读取datetime:
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print('strptime:', cday)

# # 把datetime格式化输出:
# print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# # 对日期进行加减:
# print('current datetime =', cday)
# print('current + 10 hours =', cday + timedelta(hours=10))
# print('current - 1 day =', cday - timedelta(days=1))
# print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# # 把时间从UTC+0时区转换为UTC+8:
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print('UTC+0:00 now =', utc_dt)
# print('UTC+8:00 now =', utc8_dt)

# from collections import namedtuple

# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print('Point:', p.x, p.y)

# from collections import deque

# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# from collections import defaultdict

# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print('dd[\'key1\'] =', dd['key1'])
# print('dd[\'key2\'] =', dd['key2'])

# from collections import Counter
# c = Counter()
# for ch in 'programming':
#     c[ch] = c[ch] + 1
# print(c)

# from collections import Counter
# c = Counter('programming')
# print(c)

# c = Counter()
# c.update('programming')
# print(c)

# import base64

# s = base64.b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
# print(s)
# print(str(s,'utf-8'))

# d = base64.b64decode(s).decode('utf-8')
# print(d)

# s = base64.urlsafe_b64encode('在Python中使用BASE 64编码'.encode('utf-8'))
# print(s)
# d = base64.urlsafe_b64decode(s).decode('utf-8')
# print(d)

# import struct

# bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# print(struct.unpack('<ccIIIIIIHH', bmp_header))

import hashlib

# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())

# sha1 = hashlib.sha1()
# sha1.update('how to use sha1 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# import hmac
# message = b'Hello, world!'
# key = b'secret'
# h = hmac.new(key, message, digestmod='MD5')
# print(h.hexdigest())

# import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#     if n >= 100:
#         break

# cs = itertools.cycle('ABC')
# t = 10
# for c in cs:
#     print(c)
#     t = t - 1
#     if t == 0:
#         break

# import chardet
# data = '离离原上草，一岁一枯荣'.encode('utf-8')
# print(chardet.detect(data))

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

