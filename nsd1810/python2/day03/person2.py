class Weapon:
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

class Mage:
    def __init__(self, name, weapon_name, weapon_strength):
        self.name = name
        self.weapon = Weapon(weapon_name, weapon_strength)

    def speak(self, words):
        print(words)

if __name__ == '__main__':
    m1 = Mage('奇异博士', '时间宝石', 1000)
    m1.speak('大家好，我是%s' % m1.name)
    print(m1.weapon.name, m1.weapon.strength)
