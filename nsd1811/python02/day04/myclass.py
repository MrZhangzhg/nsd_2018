class A:
    def func1(self):
        print('a func')

    def func(self):
        print('aaaaaaaa')

class B:
    def func2(self):
        print('b func')

    def func(self):
        print('BBBBBBBBBB')

class C(B, A):  # 父类可以有多个
    def func3(self):
        print('c func')

    def func(self):
        print('CCCCCCCCCCC')

if __name__ == '__main__':
    c1 = C()  # c1具有ABC三个类的方法
    c1.func1()
    c1.func2()
    c1.func3()
    c1.func()  # 同名方法查找的顺序是自下向上，自左向右
