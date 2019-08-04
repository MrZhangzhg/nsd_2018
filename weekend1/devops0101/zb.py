import os
import time

print('starting...')
retval = os.fork()

if retval:
    print('in parent')
    time.sleep(30)
    print('parent done')
else:
    print('in child')
    time.sleep(10)
    print('child done')
    exit()
