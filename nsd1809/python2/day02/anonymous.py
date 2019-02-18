import random

def func1(x):   # 接收整数作为参数
    return x % 2    # 1为True，0为False

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    # [36, 73, 74, 50, 44, 41, 45, 79, 72, 74]
    print(nums)
    # filter的第一个参数是函数，nums中各项将会当成func1的参数
    # 经过func1的计算，如果返回值是True则保留，False舍弃
    # result = filter(func1, nums)
    # result2 = filter(lambda x: x % 2, nums)
    # print(list(result))
    # print(list(result2))
    result3 = map(func2, nums)  # map用func2函数加nums每个数字加工一遍并且保留结果
    result4 = map(lambda x: x * 2 + 1, nums)
    print(list(result3))
    print(list(result4))





