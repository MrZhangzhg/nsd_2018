fib = [0, 1]

for i in range(8):
    fib.append(fib[-1] + fib[-2])  # 列表中追加的数字是列表最后两项之和

print(fib)
