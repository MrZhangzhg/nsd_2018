import time
import os

def add(n=50000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(2):
        retval = os.fork()
        if not retval:
            add()
            exit()
    for i in range(2):
        os.waitpid(-1, 0)
    end = time.time()
    print(end - start)
