import random

tries = 0   # 设置计数器，用户最多猜3次
number = random.randint(1, 10)

while tries < 3:
    answer = int(input('猜数(1-10):'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break
    tries += 1
else:  # 循环正常结束才执行else子句，如果循环被break，else不执行
    print('数字是：', number)
