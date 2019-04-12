def gen_fib():
    fib = [0, 1]
    n = int(input('长度: '))

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    # print(fib)
    return fib   # 函数运算的结果需要使用return返回值，否则返回None

mylist = gen_fib()
print(mylist)
new_list = [10 + i for i in mylist]
print(new_list)
