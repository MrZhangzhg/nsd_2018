import time

def add(n=40000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    add()
    add()
    end = time.time()
    print(end - start)
