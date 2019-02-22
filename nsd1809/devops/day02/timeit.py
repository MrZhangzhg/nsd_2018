import time
import os
import threading

def add(n=20000000):
    result = 0
    for i in range(n):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    # for i in range(5):
    #     add()

    # for i in range(5):
    #     ret_val = os.fork()  # 创建两个子进程，分别计算
    #     if not ret_val:
    #         add()
    #         exit()

    # for i in range(5):
    #     os.waitpid(-1, 0)  # 一个waitpid只能挂起处理一个子进程
    tlist = []
    for i in range(5):
        t = threading.Thread(target=add)
        t.start()
        tlist.append(t)  # 把线程存入列表
    for t in tlist:  # 在列表中取出线程
        t.join()     # 挂载主线程，等待工作线程结束
    end = time.time()
    print(end - start)
