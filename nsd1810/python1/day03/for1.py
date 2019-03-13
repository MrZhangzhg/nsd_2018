astr = 'hello'
alist = [10, 20, 30]
atuple = ('kenji', 'chihiro')
adict = {'name': 'natasha', 'age': 18}

for ch in astr:   # 每次将一个字符赋值给ch
    print(ch)

for i in alist:    # 每次将列表中的一个数字赋值给i
    print(i)

for name in atuple:   # 每次将元组中的一个字符串赋值给name
    print(name)

for key in adict:    # 每次将字典的键赋值给key
    print('%s: %s' % (key, adict[key]))
