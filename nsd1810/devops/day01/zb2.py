import os
import time

print('start...')
retval = os.fork()
if retval:
    print('父进程')
    result = os.waitpid(-1, 0)  # -1表示与wait函数相同，0表示挂起父进程
    print(result) # 直到僵尸进程被处理才会向下执行，result值是(僵尸进程ID，状态值)
    time.sleep(10)
    print('父进程，结束')
else:
    print('子进程')
    time.sleep(20)
    print('子进程，结束')
    exit()