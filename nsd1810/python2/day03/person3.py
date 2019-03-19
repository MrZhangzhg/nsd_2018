class Mage:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def speak(self, words):
        print(words)

    def move(self):
        print('I can fly.')

class Wizard(Mage):
    pass

class Sorceress(Mage):
    pass

if __name__ == '__main__':
    harry = Wizard('哈利波特', '法杖')
    herm = Sorceress('赫敏', '女法杖')
    harry.move()
    herm.move()
