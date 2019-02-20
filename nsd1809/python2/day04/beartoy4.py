class Bear:
    def __init__(self, color, size):
        self.color = color  # 把属性绑定到具体的实例
        self.size = size

    def sing(self):
        print("My color is %s, Lalala" % self.color)

class NewBear(Bear):  # NewBear的父类(基类)是Bear
    def __init__(self, name, color, size):
        # Bear.__init__(self, color, size)
        super(NewBear, self).__init__(color, size)  # 推荐写法
        self.name = name

    def run(self):
        print('I can run......')

if __name__ == '__main__':
    bear1 = NewBear('熊大', 'Brown', 'Middle')
    bear1.sing()  # 子类直接拥有父类的方法
    bear1.run()
    print(bear1.name)
