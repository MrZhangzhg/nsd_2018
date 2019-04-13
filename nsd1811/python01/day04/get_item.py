alist = ['tom', 'bob', 'jerry', 'alice']

for i in [0, 1, 2, 3]:
    print('%s: %s' % (i, alist[i]))

for i in range(4):
    print('%s: %s' % (i, alist[i]))

for i in range(len(alist)):   # 常用
    print('%s: %s' % (i, alist[i]))

for item in enumerate(alist):
    # [(0, 'tom'), (1, 'bob'), (2, 'jerry'), (3, 'alice')]
    print('%s: %s' % item)

for ind, name in enumerate(alist):  # 常用
    print('%s: %s' % (ind, name))

