import os
import time


def show_time(format='%H:%M:%S'):
    pwd = os.getcwd()
    print(pwd)
    print(time.strftime(format))


if __name__ == '__main__':
    show_time()

# PEP
