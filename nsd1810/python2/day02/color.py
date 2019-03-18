def set_color(func):
    def red():
        return '\033[31;1m%s\033[0m' % func()

    return red

def hello():
    return 'Hello World!'

@set_color
def greet():
    return 'How are you?'

if __name__ == '__main__':
    a = set_color(hello)
    print(a())
    print(greet())
    # print(set_color(greet)())
# greet因为有装饰器，所有这里的greet其实是把greet函数作为set_color的参数传进去
# 返回red，有装饰器的greet相当于是set_color(greet)()
