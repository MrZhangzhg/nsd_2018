import os
import time

print('start...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(60)
else:
    print('子进程')
    time.sleep(15)
    exit()   # 进程执行exit后将彻底结束

print('Done')

# watch -n1 ps a
