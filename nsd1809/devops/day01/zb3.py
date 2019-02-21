import os
import time

ret_val = os.fork()
if ret_val:
    print('父进程')
    time.sleep(5)
    result = os.waitpid(-1, 1)  # 不挂起父进程
    print(result)  # (0, 状态)
    time.sleep(50)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(20)
    print('子进程结束')
    exit()
