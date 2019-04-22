import time
import threading
import os

def myadd():
    result = 0
    for i in range(1, 20000001):
        result += i
    print(result)

if __name__ == '__main__':
    start1 = time.time()
    for i in range(2):
        myadd()
    end1 = time.time()
    print(end1 - start1)
###################################
    start2 = time.time()
    for i in range(2):
        retval = os.fork()
        if not retval:
            myadd()
            exit()
    # 因为创建了两个子进程，每个waitpid只能监听一个子进程，挂起两次要执行两次waitpid
    for i in range(2):
        os.waitpid(-1, 0)
    end2 = time.time()
    print(end2 - start2)
###################################
    start3 = time.time()
    t1 = threading.Thread(target=myadd)
    t1.start()
    t2 = threading.Thread(target=myadd)
    t2.start()
    t1.join()
    t2.join()
    end3 = time.time()
    print(end3 - start3)
