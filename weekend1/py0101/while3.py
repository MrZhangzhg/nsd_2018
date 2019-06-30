import random

num = random.randint(1, 100)   # 随机取出1到10之间的整数

while True:
    answer = int(input('guess: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
