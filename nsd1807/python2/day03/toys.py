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

if __name__ == '__main__':
    bear_big = BearToy('Large', 'Brown')   # 实例化，bear_big自动作为第一个参数传递
    print(bear_big.vendor.phone)
    bear_big.vendor.dial()
    vendor = Vendor('400-800-1234')
    print(vendor.phone)
    # print(bear_big.size)
    # print(bear_big.color)
    # bear_big.sing()
    # tidy = BearToy('Small', 'Orange')
    # tidy.sing()
