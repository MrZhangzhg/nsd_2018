hi = 'Hello World'

def pstar(n=30):
    print('*' * n)

if __name__ == '__main__':
    pstar()   # 调用函数时，没有指定参数，就使用函数默认的参数值
    pstar(50)
