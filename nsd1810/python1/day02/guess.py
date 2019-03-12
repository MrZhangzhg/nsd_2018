import random

num = random.randint(1, 3)   # 随机生成1到3之间的一个整数
result = int(input('guess the number: '))

if result > num:
    print('猜大了')
elif result < num:
    print('猜小了')
else:
    print('猜对了')

print('正确的数字:', num)
