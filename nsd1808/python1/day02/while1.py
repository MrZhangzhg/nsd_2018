# result = 0   # 用于保存计算结果
# counter = 1    # 计数器，不断累加到result中
#
# while counter <= 100:
#     result += counter
#     counter += 1
#
# print(result)
#############################
#
result = 0
counter = 0

while counter < 100:
    counter += 1
    # if counter % 2 == 1:
    if counter % 2:   # 余数为1或0，1为真0为假
        continue
    # else:
    result += counter

print(result)
