class Foo:
    def hello(self):
        print('hello world')

class Bar:
    def welcome(self):
        print('how are you?')

class FooBar(Foo, Bar):
    '子类有多个父类，它将继承所有父类的方法'
    pass

if __name__ == '__main__':
    mc1 = FooBar()
    mc1.welcome()
    mc1.hello()
