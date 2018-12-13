# def foo():
#     print('in foo')
#     bar()
#
# def bar():
#     print('in bar')
#
# foo()
##########################
# def myfunc(*args):   # *标识args是个元组
#     print(args)
#
# def myfunc2(**kwargs):  # **标识kwargs是字典
#     print(kwargs)
#
# if __name__ == '__main__':
#     myfunc()
#     myfunc(10)
#     myfunc(10, 20, 30)
#     myfunc(10, 20, 30, 'bob', 'tom')
#     myfunc2(name='bob')
#     myfunc2(name='bob', age=23)
##########################
def add(x, y):
    print(x + y)

if __name__ == '__main__':
    alist = [10, 20]
    add(*alist)    # 调用函数时，参数加上*表示将序列对象拆开
    add(*'ab')










