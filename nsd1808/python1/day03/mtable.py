# for i in range(3):   # 控制行 [0, 1, 2]
#     for j in range(i + 1):  # 控制行内的hello
#         print('hello', end='')   # 抑制print自带的回车
#     print()

for i in range(1, 10):   # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(1, i + 1):  # j取值的列表，每次都不一样，每次都从1开始
        print('%sX%s=%s' % (j, i, i * j), end=' ')
    print()
