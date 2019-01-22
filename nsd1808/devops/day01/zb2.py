import os
import time

print('start...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(20)
    result = os.waitpid(-1, 0)  # 挂起父进程，直到子进程结束，处理子进程后继续
    print(result)   # 值是一个元组：(子进程pid，状态)
    time.sleep(20)
    print('parent done')
else:
    print('in child')
    time.sleep(40)
    print('child done')
