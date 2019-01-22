import os

print('Hello World!')

ret_val = os.fork()
if ret_val:
    print('Hello from parent')
else:
    print('Hello from child')

print('Hello from both')
