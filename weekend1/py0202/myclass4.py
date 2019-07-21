class A:
    def funca(self):
        print('funca')

    def foo(self):
        print('A foo')

class B:
    def funcb(self):
        print('funcb')

    def foo(self):
        print('B foo')

class C(B, A):
    def funcc(self):
        print('funcc')

    # def foo(self):
    #     print('C foo')

if __name__ == '__main__':
    c1 = C()
    c1.funca()
    c1.funcb()
    c1.funcc()
    c1.foo()
