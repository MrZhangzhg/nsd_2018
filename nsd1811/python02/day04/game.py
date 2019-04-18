class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, content):
        print('我是%s，%s' % (self.name, content))

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画㦸')  # 自动调用__init__
    gy = Warrior('关羽', '冷艳锯')
    print('我是%s，我用的武器是%s' % (lb.name, lb.weapon))
    print('我是%s，我用的武器是%s' % (gy.name, gy.weapon))
    lb.speak('人在塔在！')
    gy.speak('过五关，斩六将！')

# __init__是构造方法，当实例化时自动调用
# 方法只不过就是类中的函数而已
# 实例化时，实例自动作为第一个参数传递给__init__方法
# self只是一个变量名，名字也可以是其他名字，只是在python中习惯起名为self
# 拥有self(绑定到实例上的属性)，在类中任何位置均可用
# 没有绑定到实例上的，只是局部变量，只能在方法内部使用
