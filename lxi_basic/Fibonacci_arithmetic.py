# 使用Python实现Fibonacci
def fib(n):
    a, b = 1, 1
    for i in range(n):
    print(a, end=' ')
    a, b = b, a+b
    if a>n:
        break
fib(100) #输出的是100以内的斐波那契数列
i = 1
j = 1
print(i,j)
for x in range(2,100):
    if x == i + j:
        print(x)
        j = i
        i = x