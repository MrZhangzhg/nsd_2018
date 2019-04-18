class Warrior:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, content):
        print('我是%s，%s' % (self.name, content))

class MaleWarrior(Warrior):  # 括号中指定父类(基类)
    def attack(self):
        print('attack')

if __name__ == '__main__':
    lb = MaleWarrior('吕布', '方天画㦸')
    lb.speak('aaaa')
    lb.attack()
