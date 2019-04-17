def deco(func):
    def red():
        return '\033[31;1m%s\033[0m' % func()

    return red

def hello():
    return 'Hello World!'

@deco
def greet():
    return 'ni hao'

if __name__ == '__main__':
    print(hello())
    a = deco(hello)   # 将hello函数作为参数传递给deco，deco的返回值是red函数
    print(a())  # 调用a函数，实际上是调用red函数
    print(greet())
