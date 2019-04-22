import os
import time

print('start')
retval = os.fork()
if retval:
    print('父进程')
    # 挂起父进程，子进程变成僵尸进程，处理后才继续向下执行
    result = os.waitpid(-1, 0)
    print(result)
else:
    print('子进程')
    time.sleep(10)
    exit()

time.sleep(5)
print('Done')
