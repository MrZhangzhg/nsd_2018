# def add(x, y):
#     return x + y
#
# if __name__ == '__main__':
#     print(add(10, 20))
#     myadd = lambda x, y: x + y
#     print(myadd(10, 20))

from random import randint

def func1(num):
    return num % 2   # 返回值是1即为True，返回值是0即为False

if __name__ == '__main__':
    alist = [randint(1, 100) for i in range(20)]
    print(alist)  # [47, 57, 19, 39, 91, 71, 44]
    result = filter(func1, alist)
    print(list(result))
    # filter将它第2个参数中的每一项，作为第一个参数(函数)的参数传递
    # 如果func1的返回值是True就留下来，否则过滤掉
    result2 = filter(lambda num: num % 2, alist)
    print(list(result2))



