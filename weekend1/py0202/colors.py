def deco(func):
    def set_color():
        return '\033[31;1m%s\033[0m' % func()
    return set_color

def hello():
    return 'hello world'

@deco
def welcome():
    return 'welcome'

if __name__ == '__main__':
    # print(hello())
    # print(welcome())
    # print(set_color(hello))
    # print(set_color(welcome))
    hello = deco(hello)
    print(hello())
    print(welcome())
