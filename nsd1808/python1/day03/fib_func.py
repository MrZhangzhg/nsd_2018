def gen_fib(length):  # 函数需要处理的数据，用参数传进去
    fib = [0, 1]

    for i in range(length - 2):
        fib.append(fib[-1] + fib[-2])

    return fib     # 函数执行结束后，用return返回处理结果，没有return，返回None

a = gen_fib(10)
print(a)
n = int(input('长度: '))
b = gen_fib(n)
with open('/tmp/fib.txt', 'w') as fobj:
    fobj.write(str(b))   # 文件只能写字符串
