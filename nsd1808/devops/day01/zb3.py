import os
import time

print('start...')
ret_val = os.fork()
if ret_val:
    print('in parent')
    time.sleep(20)
    result = os.waitpid(-1, 1)  # 不挂起父进程
    print(result)   # 值是一个元组：(0，状态)
    time.sleep(20)
    print('parent done')
else:
    print('in child')
    time.sleep(30)
    print('child done')
