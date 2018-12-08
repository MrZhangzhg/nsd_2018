fib = [0, 1]

# 向fib列表追加元素，追加的元素总是列表中最后两个数字之和
for i in range(8):
    fib.append(fib[-1] + fib[-2])

print(fib)
