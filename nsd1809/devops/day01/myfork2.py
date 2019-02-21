import os

for i in range(3):
    ret_val = os.fork()
    if not ret_val:  # 如果是子进程
        print('Hello World!')
        exit()  # 进程遇到exit后，就彻底结束了

print('done')
