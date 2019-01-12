import random

number = random.randint(1, 10)   # 生成1－10之间的数字，可以包括1和10

while True:
    answer = int(input("number: "))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break   # 结束循环，跳到循环语句下面的代码分，继续运行

print('Done')
