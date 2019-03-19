import time

def timeit(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start)

def func1():
    print('func start')
    time.sleep(3)
    print('func end')

if __name__ == '__main__':
    timeit(func1)
