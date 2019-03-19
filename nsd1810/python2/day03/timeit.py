import time

def deco(func):
    def timeit():
        start = time.time()
        func()
        end = time.time()
        print(end - start)
    return timeit

@deco
def func1():
    print('func start')
    time.sleep(3)
    print('func end')

def func2():
    print('func start')
    time.sleep(3)
    print('func end')

if __name__ == '__main__':
    func1()
    deco(func2)()
