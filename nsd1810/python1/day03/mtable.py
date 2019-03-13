# for i in range(3):
#     print('hello')

# for i in range(3):   # 控制打印几行
#     for j in range(3):   # 控制行内打印多少次
#         print('hello', end=' ')  # print语句默认打印回车，需要使用end把回车取消
#     print()   # 一行内，打印3个hello后再打印回车

# for i in range(3):
#     for j in range(i + 1):  # 第1行打印1个hello，第i行打印i个hello
#         print('hello', end=' ')
#     print()  # print本身就可以打印一个回车

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%sx%s=%s' % (j, i, i * j), end=' ')
    print()
