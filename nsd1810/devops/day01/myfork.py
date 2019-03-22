import os

print('starting...')
retval = os.fork()  # os.fork对于父进程返回值是非0值；子进程的返回值是0
# 后续代码在父子进程都会执行
if retval:
    print('hello from parent')
else:
    print('hello from child')

print('Hello World!')
