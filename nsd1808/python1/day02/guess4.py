import random

number = random.randint(1, 3)   # 生成1－10之间的数字，可以包括1和10
counter = 0

while counter < 3:
    answer = int(input("number: "))
    if answer > number:
        print('猜大了')
    elif answer < number:
        print('猜小了')
    else:
        print('猜对了')
        break
    counter += 1
else:  # 循环正常结束时执行，如果被break也就不执行了
    print('answer:', number)

