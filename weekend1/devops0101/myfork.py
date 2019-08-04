import os

print('starting...')

# os.fork()的返回值，在父进程中是非0值(子进程的pid)，子进程中是0
retval = os.fork()
if retval:
    print('hello from parent')
else:
    print('hello from child')

print('hello from both!')
