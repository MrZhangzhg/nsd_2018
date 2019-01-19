class PigToy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def show_me(self):
        print('Hi, my name is %s, I am %s' % (self.name, self.color))

class NewPigToy(PigToy):
    def __init__(self, name, color, size):
        # PigToy.__init__(self, name, color)
        super(NewPigToy, self).__init__(name, color)
        self.size = size

    def walk(self):
        print('walking...')

a = NewPigToy('piggy', 'pink', 'Middle')
print(a.name, a.size)
