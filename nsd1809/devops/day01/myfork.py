import os

# print('starting...')
# os.fork()
# print('Hello World!')

print('starting...')
ret_val = os.fork()
# os.fork的返回值：子进程返回0，父进程是非0值(子进程ID)
if ret_val:
    print('Hello from parent')
else:
    print('Hello from child')

print('Hello from both')
