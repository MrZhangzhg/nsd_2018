import random

number = random.randint(1, 100)   # 生成1-100间的随机数字，包含1和100
print('number -> ', number)
answer = int(input('猜数(1-100):'))   # 将用户输入的字符数字转成真正的数字

if answer > number:
    print('猜大了')
elif answer < number:
    print('猜小了')
else:
    print('猜对了')
