import random

number = random.randint(1, 100)
running = True

while running:
    answer = int(input('猜数(1-100):'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        running = False
