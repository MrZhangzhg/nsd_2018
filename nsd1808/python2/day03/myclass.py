class A:
    def foo(self):
        print('foo')
    def hi(self):
        print('hello')

class B:
    def bar(self):
        print('bar')
    def hi(self):
        print('你好')

class C(B, A):   # 子类可以有多个父类，继承所有父类的方法
    def hi(self):
        print('ni hao')

c1 = C()
c1.foo()
c1.bar()
c1.hi()   # 方法查找顺序是自下向上，自左向右
