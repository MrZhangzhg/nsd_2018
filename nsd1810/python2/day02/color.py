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
