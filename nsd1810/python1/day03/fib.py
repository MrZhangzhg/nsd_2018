fib = [0, 1]

# for i in range(8):
#     fib.append(fib[-1] + fib[-2])  # 每次将列表中最后两项之和追加到列表中
#
# print(fib)

num = int(input('数列长度: '))
for i in range(num - 2):
    fib.append(fib[-1] + fib[-2])

print(fib)

