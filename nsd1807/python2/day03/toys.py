class Vendor:
    def __init__(self, phone):
        self.phone = phone

    def dial(self):
        print('calling %s' % self.phone)

class BearToy:
    def __init__(self, size, color):
        '实例化一个对象时，自动调用'
        self.size = size    # bear_big.size = 'Large'
        self.color = color  # bear_big.color = 'Brown'
        self.vendor = Vendor('400-800-1234')

    def sing(self):
        print('My color is %s, Lalala...' % self.color)

class NewBearToy(BearToy):   # 括号中填入的是父类、基类
    def __init__(self, name, size, color):
        # BearToy.__init__(self, size, color)
        super(NewBearToy, self).__init__(size, color)
        self.name = name

    def walk(self):
        print('I can walk.')

if __name__ == '__main__':
    bear2 = NewBearToy('bear2', 'Middle', 'Brown')
    print(bear2.name)
    bear2.sing()
    bear2.walk()

    # bear_big = BearToy('Large', 'Brown')   # 实例化，bear_big自动作为第一个参数传递
    # print(bear_big.vendor.phone)
    # bear_big.vendor.dial()
    # vendor = Vendor('400-800-1234')
    # print(vendor.phone)
    # print(bear_big.size)
    # print(bear_big.color)
    # bear_big.sing()
    # tidy = BearToy('Small', 'Orange')
    # tidy.sing()
