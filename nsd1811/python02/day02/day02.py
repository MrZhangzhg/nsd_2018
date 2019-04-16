def func1(*args):
    # args前面的*号，表明args是元组，传参会把参数放入元组
    print(args)

def func2(**kwargs):
    # kwargs前面的**号，表明kwargs是字典
    print(kwargs)

if __name__ == '__main__':
    func1()
    func1('hao')
    func1('hao', 123)
    func2()
    func2(name='tom', age=20)
