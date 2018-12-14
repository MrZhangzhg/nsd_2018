def set_color(func):
    def set_red():
        return '\033[31;1m%s\033[0m' % func()
    return set_red

def hello():
    return 'Hello World'

@set_color
def welcome():
    return 'Hello China'

@set_color
def mytest():
    a = 10 + 10
    return a

if __name__ == '__main__':
    # print(hello())
    # print(welcome())
    hello = set_color(hello)
    print(hello())
    print(welcome())
    print(mytest())
