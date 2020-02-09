# 定义一个函数求一元二次方程但两个解
import sys
from math import *
# 参数a,b,c应该均为整数或浮点数，b**2-(4*a*c)应大于等于零
def quadratic(a,b,c):
    x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
    return x1,x2
# 检查参数a,b,c点数据类型，不符合类型时抛出异常，终止程序。
a,b,c = input('请输入一元二次方程组的三个参数a,b,c,以空格分隔：').split()
try:
    a = float(a)
except ValueError:
    print("Input is not a float")
    sys.exit()
try:
    b = float(b)
except ValueError:
    print("Input is not a float")
    sys.exit()
try:
    c = float(c)
except ValueError:
    print("Input is not a float")
    sys.exit()
# print("a:%.2f,b:%.2f,c:%.2f" %(a,b,c))
# 方程求解
if b ** 2 - (4 * a * c) >= 0:
    x1,x2= quadratic(a,b,c)
    print("一元二次方程的两个解：",'x1:%.2f,x2:%.2f' %(x1,x2))
else:
    print('该方程无实数解')