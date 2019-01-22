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

# watch -n1 ps a


