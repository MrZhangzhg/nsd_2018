# 最多猜4次
import random

num = random.randint(1, 10)
counter = 0

while counter < 4:
    result = int(input('guess the number: '))

    if result > num:
        print('猜大了')
    elif result < num:
        print('猜小了')
    else:
        print('猜对了')
        break

    counter += 1
else:  # 循环的else语句，如果循环被break中断，else不执行，否则执行
    print('正确的数字:', num)
