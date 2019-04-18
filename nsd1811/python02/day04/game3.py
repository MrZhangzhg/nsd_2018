class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Warrior:
    def __init__(self, name, wname, wstrength):
        self.name = name
        self.weapon = Weapon(wname, wstrength)

    def speak(self, content):
        print('我是%s，%s' % (self.name, content))

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画㦸', 100)
    print(lb.weapon)
    print(lb.weapon.name, lb.weapon.strength)
