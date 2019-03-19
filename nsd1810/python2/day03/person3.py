class Mage:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print(words)

    def move(self):
        print('I can fly.')

class Wizard(Mage):
    def __init__(self, name, weapon, clothes):
        self.name = name
        self.weapon = weapon
        self.clothes = clothes

    def ride(self, zuoji):
        print('I am %s, I can ride %s' % (self.name, zuoji))

class Sorceress(Mage):
    def __init__(self, name, weapon, clothes):
        # Mage.__init__(self, name, weapon)
        super(Sorceress, self).__init__(name, weapon)
        self.clothes = clothes

if __name__ == '__main__':
    harry = Wizard('哈利波特', '法杖', '男式衣服')
    herm = Sorceress('赫敏', '女法杖', '女式衣服')
    harry.move()
    herm.move()
    print(harry.clothes)
    harry.ride('扫帚')
    harry.ride('龙')
