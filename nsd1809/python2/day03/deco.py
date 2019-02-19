def set_color(func):
    def color():
        return '\033[31;1m%s\033[0m' % func()
    return color

def hello():
    return 'Hello World!'

@set_color
def welcome():
    return 'Hello China!'

if __name__ == '__main__':
    # a = set_color(hello)
    # print(a())
    hello = set_color(hello)
    print(hello())
    print(welcome)   # 调用set_color(welcome)  返回内层函数color
    print(welcome())  # 此处的调用，实际上是调用内层的color

