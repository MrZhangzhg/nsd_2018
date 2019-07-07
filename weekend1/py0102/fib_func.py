# def gen_fib():
#     fib = [0, 1]
#     n = int(input('length: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     print(fib)
#
# a = gen_fib()   # 函数默认返回None
# print(a)

# def gen_fib():
#     fib = [0, 1]
#     n = int(input('length: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#
#     return fib   # 函数的运算结果，通守return进行返回
#
# a = gen_fib()
# print(a)


def gen_fib(n=8):   # 定义形参n
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib   # 函数的运算结果，通守return进行返回

print(gen_fib())

for i in range(5, 16, 2):
    a = gen_fib(i)
    print(a)

n = int(input('length: '))
print(gen_fib(n))

