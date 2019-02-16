import time

counter = 19
n = 0
print('#' * 20, end='')

while True:
    n += 1
    print('\r%s@%s' % ('#' * n, '#' * (counter - n)), end='')
    time.sleep(0.3)
    if n == counter:
        n = 0
