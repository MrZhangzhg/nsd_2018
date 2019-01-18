def deco(func):
    def color():
        return "\033[31;1m%s\033[0m" % func()
    return color

def hello():
    return 'Hello World!'

@deco
def welcome():
    return 'Hello China!'

if __name__ == '__main__':
    a = deco(hello)
    print(a())
    hello = deco(hello)
    print(hello())
    print(welcome())

