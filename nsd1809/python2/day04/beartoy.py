class Bear:  # 定义类
    def __init__(self, color, size):
        "在实例化的时候，自动调用。实例自动当成第一个参数"
        self.color = color  # 把属性绑定到具体的实例
        self.size = size

    def sing(self):
        print("My color is %s, Lalala" % self.color)

if __name__ == '__main__':
    bear_big = Bear('Brown', 'Large')   # 创建实例
    print(bear_big.color, bear_big.size)
    bear_big.sing()  # 实例bear_big自动当成第一个参数传递

    bear2 = Bear('Brown', 'Middle')
    bear2.sing()
