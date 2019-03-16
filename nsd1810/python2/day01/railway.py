import time

n = 0
print('#' * 20, end='')

while True:
    time.sleep(0.2)
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')
    n += 1
    if n == 20:
        n = 0
