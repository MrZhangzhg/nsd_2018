# fib = [0, 1]
# 数列中总是把最后两个数之和追加到列表
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
#
# print(fib)

fib = [0, 1]
n = int(input('length: '))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)


