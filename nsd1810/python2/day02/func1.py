def func1(*args):    # *号表示后面的名字是个元组
    print(args)

def func2(**kwargs):   # **号表示后面的名字是字典
    print(kwargs)

if __name__ == '__main__':
    func1()
    func1('bob')
    func1('bob', 'tom', 'kenji', 'natasha')
    func2()
    func2(name='bob', age=20)
