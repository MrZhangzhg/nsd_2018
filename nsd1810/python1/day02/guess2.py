import random

num = random.randint(1, 10)

while True:
    result = int(input('guess the number: '))

    if result > num:
        print('猜大了')
    elif result < num:
        print('猜小了')
    else:
        print('猜对了')
        break

print('正确的数字:', num)
