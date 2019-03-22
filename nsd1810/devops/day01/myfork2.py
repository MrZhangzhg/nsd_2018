import os

for i in range(3):
    ret_val = os.fork()
    if not ret_val:
        print('Hello')
        exit()
