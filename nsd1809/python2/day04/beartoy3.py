class Bear:
    def __init__(self, color, size):
        self.color = color  # 把属性绑定到具体的实例
        self.size = size

    def sing(self):
        print("My color is %s, Lalala" % self.color)

class NewBear(Bear):  # NewBear的父类(基类)是Bear
    pass

if __name__ == '__main__':
    bear1 = NewBear('Brown', 'Middle')
    bear1.sing()  # 子类直接拥有父类的方法
