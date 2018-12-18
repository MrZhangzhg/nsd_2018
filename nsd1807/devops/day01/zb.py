import os
import time

# print('starting...')
# retval = os.fork()
# if retval:
#     print('in parent')
#     time.sleep(60)
# else:
#     print('in child')
#     time.sleep(20)
#     exit()
#
# print('done')
# watch -n1 ps a


print('starting...')
retval = os.fork()
if not retval:
    print('in child')
    time.sleep(10)
    exit()

# waitpid第一个参数-1，表示与wait函数相同；第二个参数，0表示挂起父进程，1表示不挂起
result = os.waitpid(-1, 0)  # 父进程挂起，等待子进程结束
print(result)
time.sleep(15)
print('done')



