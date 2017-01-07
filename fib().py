#斐波拉契数列:除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
    n, a, b =0 , 0, 1
    while n <max:
        print(b)
        a, b = b, a+b
        n = n+1
    return 'done'
fib(6)

#定义生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
f = fib(6)
print(f)


