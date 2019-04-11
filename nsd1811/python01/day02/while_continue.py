result = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2 == 1:
    if counter % 2:   # 结果只有1和0两种情况，1是True，0是False
        continue

    result += counter

print(result)
