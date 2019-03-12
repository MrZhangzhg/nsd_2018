result = 0     # 将从1加到100的结果保存到变量中，定义保存结果的变量
counter = 1    # 设置计数器，把计数器不断自增1，累加到result中

while counter <= 100:
    result += counter
    counter += 1

print(result)
