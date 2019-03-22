import time
import os

def add(n=20000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    add()
    add()
    add()
    add()
    end = time.time()
    print(end - start)
##########################
    # start = time.time()
    # for i in range(4):
    #     retval = os.fork()
    #     if not retval:
    #         add()
    #         exit()
    # os.waitpid(-1, 0)   # 两个子进程，需要两个waitpid挂起处理
    # os.waitpid(-1, 0)
    # os.waitpid(-1, 0)
    # os.waitpid(-1, 0)
    # end = time.time()
    # print(end - start)
