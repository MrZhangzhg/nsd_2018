# def generate_fib():
#     fib = [0, 1]
#
#     for i in range(8):
#         fib.append(fib[-1] + fib[-2])
#
#     print(fib)
#
# # generate_fib()   # 调用函数，即将函数内的代码运行一遍
# # generate_fib()
# a = generate_fib()
# print(a)   # 函数没有return语句，默认返回None
##############################
# def generate_fib():
#     fib = [0, 1]
#
#     for i in range(8):
#         fib.append(fib[-1] + fib[-2])
#
#     return fib
#
# alist = generate_fib()
# print(alist)
# blist = [i * 2 for i in alist]
# print(blist)
##############################
def generate_fib(n):
    fib = [0, 1]

    for i in range(n - 2):
        fib.append(fib[-1] + fib[-2])

    return fib

a = generate_fib(10)
print(a)
b = generate_fib(20)
print(b)
x = int(input('length: '))
c = generate_fib(x)
print(c)
