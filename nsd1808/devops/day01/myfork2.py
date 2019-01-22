import os

for i in range(7):  # [0, 1, 2]
    ret_val = os.fork()
    if not ret_val:
        print('Hello World!')
        exit()
