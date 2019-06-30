import random

num = random.randint(1, 10)   # 随机取出1到10之间的整数
counter = 0

while counter < 5:
    answer = int(input('guess: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:   # 循环被break就不执行else了，否则执行
    print('answer is:', num)
