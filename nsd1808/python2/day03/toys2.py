class Vendor:
    def __init__(self, company, ph):
        self.company = company
        self.phone = ph

    def call(self):
        print('Calling %s...' % self.phone)

class PigToy:       # 定义玩具类
    def __init__(self, name, color, company, ph):
        self.name = name
        self.color = color
        self.vendor = Vendor(company, ph)

    def show_me(self):
        print('Hi, my name is %s, I am %s' % (self.name, self.color))

piggy = PigToy('Piggy', 'pink', 'tedu', '400-800-1234')    # 创建实例
# piggy.show_me()
print(piggy.vendor.company)
piggy.vendor.call()
