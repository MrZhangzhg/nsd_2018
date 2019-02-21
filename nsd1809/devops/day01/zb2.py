import os
import time

ret_val = os.fork()
if ret_val:
    print('父进程')
    result = os.waitpid(-1, 0)  # 挂起父进程，直到子进程结束
    print(result)  # (子进程PID, 状态)
    time.sleep(20)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(30)
    print('子进程结束')
    exit()
