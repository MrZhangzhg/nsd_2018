import os
import time

print('start...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(30)
    print('父进程，结束')
else:
    print('子进程')
    time.sleep(20)
    print('子进程，结束')
    exit()
# watch -n1 ps a   # 每隔1秒运行ps a

