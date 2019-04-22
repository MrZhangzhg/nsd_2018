import threading
import time

def say_hi():
    print('Hello World!')
    time.sleep(3)
    print('Done')

if __name__ == '__main__':
    print('start')
    t1 = threading.Thread(target=say_hi)  # 创建工作线程
    t1.start()  # 启动工作线程，将会执行target() => say_hi()
    t2 = threading.Thread(target=say_hi)
    t2.start()
