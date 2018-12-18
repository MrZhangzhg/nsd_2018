import os

# print('开始')
# os.fork()
# print('你好')

# print('start')
# a = os.fork()
# if a:
#     print('in parent')
# else:
#     print('in child')
#
# print('end')

for i in range(3):
    retval = os.fork()
    if not retval:
        print('hello world!')
        exit()   # 一旦遇到exit，进程将彻底结束












