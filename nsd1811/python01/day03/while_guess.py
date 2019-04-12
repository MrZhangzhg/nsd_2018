import random

num = random.randint(1, 10)
counter = 0

while counter < 3:
    counter += 1
    answer = int(input('guess the number: '))
    if answer > num:
        print('猜大了')
    elif answer < num:
        print('猜小了')
    else:
        print('猜对了')
        break
else:  # 如果循环执行了break，则不再执行else，否则需要执行
    print('正确的结果是：%s' % num)
