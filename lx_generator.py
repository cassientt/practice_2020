# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# f = fib(10)
# print('fib(10):', f)
# for x in f:
#     print(x)

# # call generator manually:
# g = fib(5)
# while 1:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

def triangles():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]
# 该方式用到了列表生成式，理解起来较困难，下面是另一种方式：
def triangles():
    ret = [1]
    while True:
        yield ret
        for i in range(1, len(ret)):
            ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
# 另一个不用生成器的版本：
def YangHui (num = 10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL