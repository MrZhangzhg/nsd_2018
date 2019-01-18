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
#
def add(x, y):
    print(x + y)

if __name__ == '__main__':
    add(10, 20)
    nums = [10, 20]
    add(nums[0], nums[1])
    add(*nums)   # *nums表示把nums拆开







