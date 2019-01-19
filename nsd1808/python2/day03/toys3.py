class PigToy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_me(self):
        print('Hi, my name is %s, I am %s' % (self.name, self.color))

class NewPigToy(PigToy):   # 新类继承它父类的所有属性
    def walk(self):
        print('walking...')

a = NewPigToy('piggy', 'pink')
a.show_me()
a.walk()
