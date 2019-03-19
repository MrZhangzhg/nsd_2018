class BearToy:
    def __init__(self, name, color, size):
        '绑定在实例上的属性，在类中任何地方都可见可用'
        self.name = name
        self.color = color
        self.size = size

    def sing(self, lyrics):
        '方法自己的参数、变量是局部变量，只有在该方法中可用'
        print('I am %s, %s' % (self.name, lyrics))

if __name__ == '__main__':
    # 创建实例时，自动调用__init__方法
    # 实例名bear1会自动作为第一个参数传给self
    bear1 = BearToy('熊大', 'Brown', 'Large')
    bear2 = BearToy('熊二', 'Brown', 'Middle')
    print(bear1.name, bear1.color, bear1.size)
    bear1.sing('Lalala')
    bear2.sing('Hahaha')
