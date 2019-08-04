import os

for i in range(3):
    retval = os.fork()
    if not retval:
        print('hello world')
        exit()
