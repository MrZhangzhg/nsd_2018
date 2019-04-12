# fib = [0, 1]
#
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])  # 将列表中最后两项之和，追加到列表中
#
# print(fib)
###############################
fib = [0, 1]
n = int(input('长度: '))

for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)
