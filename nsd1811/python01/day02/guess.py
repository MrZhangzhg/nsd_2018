import random

num = random.randint(1, 5)   # 随机生成1－5之间的数字
answer = int(input('guess the number: '))

print('正确的结果是：%s' % num)
if answer > num:
    print('猜大了')
elif answer < num:
    print('猜小了')
else:
    print('猜对了')
