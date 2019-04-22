import threading
import time

def say_hi(n=3):
    print('Hello World!')
    time.sleep(n)
    print('Done')

if __name__ == '__main__':
    print('start')
    t1 = threading.Thread(target=say_hi)
    t1.start()
    t1.join()  # 挂起主线程，直到t1线程结束，代码才会向下执行
    t2 = threading.Thread(target=say_hi, args=(7,))
    t2.start()
