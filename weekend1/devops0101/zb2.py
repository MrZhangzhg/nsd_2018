import os
import time

print('starting...')
retval = os.fork()

if retval:
    print('in parent')
    time.sleep(15)
    # waitpid用于处理子进程，第一个参数-1，表示与wait有相同的功能
    # 第二个参数，1表示不挂起父进程，0表示挂起
    # 处理子进程时，如果子进程是僵尸进程，则回收它的全部资源
    # 如果子进程不是僵尸进程，父进程在不挂起的情况下，会继续向下运行
    result = os.waitpid(-1, 1)
    print(result)
    time.sleep(10)
    print('parent done')
else:
    print('in child')
    time.sleep(10)
    print('child done')
    exit()
