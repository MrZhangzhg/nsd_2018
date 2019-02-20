class MyClass1:
    def hello(self):
        print('Hello World!')

    def greet(self):
        print('in class 1')

class MyClass2:
    def welcome(self):
        print('How are you?')

    def greet(self):
        print('in class 2')

class C(MyClass1, MyClass2):  # C是两个类的子类，拥有所有父类方法
    def greet(self):
        print('in C')

if __name__ == '__main__':
    mc = C()
    mc.hello()
    mc.welcome()
    mc.greet()  # 方法查找，顺序是从下向上，从左到右
