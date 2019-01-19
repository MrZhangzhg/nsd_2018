class PigToy:       # 定义玩具类
    def init(self, name, color):
        self.name = name
        self.color = color

    def show_me(self):
        print('Hi, my name is %s, I am %s' % (self.name, self.color))

piggy = PigToy()    # 创建实例
piggy.init('Piggy', 'pink')
# init(piggy, 'Piggy', 'pink')
#   piggy.name = 'Piggy'
#   piggy.color = 'pink'
piggy.show_me()
george = PigToy()
george.init('George', 'red')
george.show_me()
