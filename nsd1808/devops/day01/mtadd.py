import time
import threading

def add(n=40000000):
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)

if __name__ == '__main__':
    start = time.time()
    tlist = []
    for i in range(4):
        t = threading.Thread(target=add)
        tlist.append(t)
        t.start()
    tlist[0].join()   # 与waitpid类似，挂起主线程，直到工作线程结束
    tlist[1].join()
    tlist[2].join()
    tlist[3].join()
    end = time.time()
    print(end - start)
