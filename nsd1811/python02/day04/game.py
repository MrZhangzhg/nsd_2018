class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画㦸')  # 自动调用__init__
    gy = Warrior('关羽', '冷艳锯')
    print('我是%s，我用的武器是%s' % (lb.name, lb.weapon))
    print('我是%s，我用的武器是%s' % (gy.name, gy.weapon))

# __init__是构造方法，当实例化时自动调用
# 方法只不过就是类中的函数而已
# 实例化时，实例自动作为第一个参数传递给__init__方法
# self只是一个变量名，名字也可以是其他名字，只是在python中习惯起名为self
