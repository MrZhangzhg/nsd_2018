py_str = 'python'
alist = [10, 20, 30]
atuple = ('bob', 'alice', 'tom')
adict = {'name': 'zhangsan', 'age': 22}

for ch in py_str:
    print(ch)

for i in alist:
    print(i)

for name in atuple:
    print(name)

for key in adict:
    print('%s: %s' % (key, adict[key]))
