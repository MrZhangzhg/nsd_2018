import os
import time

print('start...')
ret_val = os.fork()
if ret_val:
    print('in parent, sleep...')
    time.sleep(40)
    print('parent done')
else:
    print('in child, sleep')
    time.sleep(20)
    print('child done')

# watch -n1 ps a  观察僵尸进程的出现
# 杀僵尸进程、杀父进程观察是否可以将其杀死


