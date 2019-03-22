import os
import time

print('start...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(5)
    result = os.waitpid(-1, 1)
    print(result)
    time.sleep(15)
    print('父进程，结束')
else:
    print('子进程')
    time.sleep(10)
    print('子进程，结束')
    exit()

print('Done')
