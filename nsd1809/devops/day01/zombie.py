import os
import time

ret_val = os.fork()
if ret_val:
    print('父进程')
    time.sleep(60)
    print('父进程结束')
else:
    print('子进程')
    time.sleep(20)
    print('子进程结束')
    exit()
# watch -n1 ps a
# 程序运行20秒后，子进程状态是Z，表示僵尸进程；60秒后父进程结束，子进程被
# systemd接管，systemd将接管的僵尸进程处理掉
