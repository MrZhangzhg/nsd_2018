import time

length = 19
count = 0

while True:
    print('\r%s@%s' % ('#' * count, '#' * (length - count)), end='')
    time.sleep(0.3)
    if count == length:
        count = 0
    count += 1

