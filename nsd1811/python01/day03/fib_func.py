def gen_fib(n=10):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    # print(fib)
    return fib   # 函数运算的结果需要使用return返回值，否则返回None

mylist = gen_fib()
print(mylist)
new_list = [10 + i for i in mylist]
print(new_list)

num = int(input('长度: '))
result = gen_fib(num)
print(result)
