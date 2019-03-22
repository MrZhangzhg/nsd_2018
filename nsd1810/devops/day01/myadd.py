import time
import os
import threading

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
##########################
    # start = time.time()
    # tlist = []  # 创建列表，存储创建的线程
    # for i in range(4):
    #     t = threading.Thread(target=add)
    #     tlist.append(t)
    #     t.start()
    # for t in tlist:  # 从列表中取出线程
    #     t.join()   # 挂起主线程，等工作线程结束后继续
    # end = time.time()
    # print(end - start)
