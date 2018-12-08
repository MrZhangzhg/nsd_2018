# for i in range(3):  # [0, 1, 2]  外层循环控制打印哪一行
#     for j in range(i + 1):  # [0] [0, 1] [0, 1, 2]  内层循环控制行内打印几次
#         print('hello', end=' ')  # 多个hello打印到同一行
#     print()  # 每一行结尾需要打印回车，否则就成为一行了
################################
for i in range(1, 10):  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(1, i + 1):  # [1], [1, 2], [1, 2 ,3]
        print('%sX%s=%s' % (j, i, i * j), end=' ')
    print()
