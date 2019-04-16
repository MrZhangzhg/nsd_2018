# def func1(*args):
#     # args前面的*号，表明args是元组，传参会把参数放入元组
#     print(args)
#
# def func2(**kwargs):
#     # kwargs前面的**号，表明kwargs是字典
#     print(kwargs)
#
# if __name__ == '__main__':
#     func1()
#     func1('hao')
#     func1('hao', 123)
#     func2()
#     func2(name='tom', age=20)
##########################################
# def add(x, y):
#     return x + y
#
# if __name__ == '__main__':
#     print(add(10, 5))
#     myadd = lambda x, y: x + y
#     print(myadd(10, 20))
##########################################
from random import randint

def func1(x):
    # x % 2的值只有1或0，1为True，0为False
    return x % 2

if __name__ == '__main__':
    nums = [randint(1, 100) for i in range(10)]
    print(nums)
    result = filter(func1, nums)
    print(list(result))
    result2 = filter(lambda x: x % 2, nums)
    print(list(result2))











