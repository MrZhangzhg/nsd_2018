class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, content):
        print('我是%s，%s' % (self.name, content))

if __name__ == '__main__':
    w = Weapon('方天画㦸', 100)
    print(w.name, w.strength)
    lb = Warrior('吕布', w)
    print(lb.weapon)
    print(lb.weapon.name, lb.weapon.strength)

