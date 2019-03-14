
alist = [10, 30, 20]

for item in enumerate(alist):   # [(0, 10), (1, 30), (2, 20)]
    print(item)

for item in enumerate(alist):
    print('%s: %s' % (item[0], item[1]))

for ind, num in enumerate(alist):
    print('%s: %s' % (ind, num))
