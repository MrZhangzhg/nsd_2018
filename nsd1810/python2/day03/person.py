class Mage:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print(words)

if __name__ == '__main__':
    m1 = Mage('奇异博士', '时间宝石')
    m1.speak('大家好，我是%s' % m1.name)
