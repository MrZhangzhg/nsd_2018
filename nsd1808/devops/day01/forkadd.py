import time
import os

def add(n=40000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    for i in range(4):
        ret_val = os.fork()
        if not ret_val:
            add()
            exit()
    print(os.waitpid(-1, 0))
    print(os.waitpid(-1, 0))
    print(os.waitpid(-1, 0))
    print(os.waitpid(-1, 0))
    end = time.time()
    print(end - start)
