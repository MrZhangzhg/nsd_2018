# def foo():
#     print('in foo')
#     bar()
#
#
# def bar():
#     print('in bar')
#
# if __name__ == '__main__':
#     foo()
###############################
#
# def myfunc(*args):    # *表示args是个元组
#     print(args)
#
# def myfunc2(**kwargs):    # **表示kwargs是个字典
#     print(kwargs)
#
# if __name__ == '__main__':
#     myfunc()   # args=()
#     myfunc('hello')   # 参数将会放到元组中 args=('hello',)
#     myfunc('hello', 123)   # args=('hello', 123)
#     myfunc2()     # kwargs={}
#     myfunc2(name='bob', age=23)   # kwargs={'name': 'bob', 'age': 23}
##############################
# #
# def add(x, y):
#     print(x + y)
#
# if __name__ == '__main__':
#     add(10, 20)
#     nums = [10, 20]
#     add(nums[0], nums[1])
#     add(*nums)   # *nums表示把nums拆开
##############################
#
# def add(x, y):
#     return x + y
#
# if __name__ == '__main__':
#     print(add(10, 20))
#
#     a = lambda x, y: x + y
#     print(a(20, 30))
##############################
#
import random

def func1(x):
    return x % 2    # 结果是1或0，表示True和Flase

def func2(x):
    return x * 2 + 1

if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    print(nums)
    # filter实现过滤，将nums中的每一项当成func1的参数，func1的结果为真，则把数字留下，否则过滤掉
    print(list(filter(func1, nums)))
    print(list(filter(lambda x: x % 2, nums)))
    # map用来加工数据，将nums中的每一个项目作为func2的参数进行加工，得到结果
    print(list(map(func2, nums)))
    print(list(map(lambda x: x * 2 + 1, nums)))











