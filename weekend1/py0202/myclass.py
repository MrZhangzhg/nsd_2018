class Role:
    def __init__(self, name, weapon):
        '一般用于将属性绑定到对象上，绑定的属性在类中任意地方可用'
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s, 我用的武器是%s' % (self.name, self.weapon))

    def speak(self, sentence):
        print(sentence)

if __name__ == '__main__':
    lb = Role('吕布', '戟')   # 自动调用__init__方法，实例lb自动作为第一个参数
    print(lb.name)
    print(lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔，人中吕布')


