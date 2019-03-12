# 计算1－100以内偶数之和
result = 0
counter = 0

while counter < 100:
    counter += 1

    # if counter % 2 == 1:
    if counter % 2:  # counter除以2的余数只有1或0，1是True，0是False
        continue

    result += counter

print(result)
