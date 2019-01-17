import time

print('#' * 20, end='')
n = 0
while True:
    time.sleep(0.3)
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
    n += 1
    if n == 20:   # 如果左边已有19个#，将n改为0
        n = 0
