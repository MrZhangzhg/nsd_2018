# import random
#
# number = random.randint(1, 100)
# answer = int(input('猜数(1-100):'))
#
# while answer != number:
#     if answer > number:
#         print('猜大了')
#     elif answer < number:
#         print('猜小了')
#     answer = int(input('猜数(1-100):'))
#
# print('猜对了')
##########################################
# DRY: Don't Repeat Yourself  不要重复你自己
import random
number = random.randint(1, 100)
while True:
    answer = int(input('猜数(1-100):'))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break
