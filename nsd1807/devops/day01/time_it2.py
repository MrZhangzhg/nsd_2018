import time
import threading

def add(n=50000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(2):
        t = threading.Thread(target=add)
        t.start()
        tlist.append(t)
    for t in tlist:
        t.join()   # 挂起，等待工作进程结束后，才会继续向下执行
    end = time.time()
    print(end - start)
