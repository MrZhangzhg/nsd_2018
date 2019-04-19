import os

# print('start')
# os.fork()  # 生成子进程，后续代码将会在父子进程中同时执行
# print('hello world!')

# print('start')
# retval = os.fork()  # 父进程的返回值是非0值(子进程的PID)，子进程的返回值是0
# if retval:
#     print('父进程')
# else:
#     print('子进程')
#
# print('both')

for i in range(3):
    retval = os.fork()
    if not retval:
        print('Hello World!')
        exit()  # 子进程执行完毕后退出，否则它将继续生成子进程
