# for i in range(3):
#     print('hello')

# for i in range(3):
#     # 外层循环控制循环到第几行，内层循环打印3个hello后，再打印回车
#     for j in range(3):
#         print('hello', end=' ')  # print默认在结尾打印\n，换成空格
#     print()

# for i in range(3):   # [0, 1, 2]
#     for j in range(i + 1):
#         print('hello', end= ' ')
#     print()

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end= ' ')
    print()
