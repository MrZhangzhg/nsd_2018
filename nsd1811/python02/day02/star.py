hi = 'Hello World!'

def pstar(n=30):
    symbol = '+'
    print('%s%s%s' % (symbol, '*' * n, symbol))

if __name__ == '__main__':
    pstar()
    print(hi)
