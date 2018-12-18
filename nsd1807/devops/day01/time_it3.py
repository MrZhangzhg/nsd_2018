import time

def add(n=50000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        add()
    end = time.time()
    print(end - start)
