chs = 'hello'
alist = ['bob', 'alice']
atuple = (10, 20)
adict = {'name': 'tom', 'age': 23}

for ch in chs:
    print(ch)

for name in alist:
    print(name)

for i in atuple:
    print(i)

for key in adict:
    print('%s: %s' % (key, adict[key]))
