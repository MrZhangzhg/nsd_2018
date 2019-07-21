class Weapon:
    def __init__(self, wname, harm):
        self.wname = wname
        self.harm = harm

class Role:
    def __init__(self, name, weapon):
        '一般用于将属性绑定到对象上，绑定的属性在类中任意地方可用'
        self.name = name
        self.weapon = weapon

    def show_me(self):
        print('我是%s, 我用的武器是%s' % (self.name, self.weapon))

if __name__ == '__main__':
    ji = Weapon('方天画戟', 100)
    lb = Role('吕布', ji)   # 自动调用__init__方法，实例lb自动作为第一个参数
    print(lb.weapon.wname)


