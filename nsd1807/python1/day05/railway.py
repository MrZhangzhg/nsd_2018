import time
import sys

n = 0
print('#' * 20, end='')

while True:
    print('\r%s@%s' % ('#' * n, '#' * (19 - n)), end='')  # \r回车不换行
    sys.stdout.flush()  # 立即在屏幕上输出，不要放到缓冲区
    n += 1
    time.sleep(0.3)
    if n == 20:
        n = 0
