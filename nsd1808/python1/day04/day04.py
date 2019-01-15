# import shutil
# shutil.copyfileobj

alist = ['bob', 'alice', 10, 20, 30]

for ind in [0, 1, 2, 3, 4]:
    print('%s: %s' % (ind, alist[ind]))

for ind in range(5):
    print('%s: %s' % (ind, alist[ind]))

for ind in range(len(alist)):    # 常用
    print('%s: %s' % (ind, alist[ind]))

print(enumerate(alist))    # 返回一个enumerate对象
print(list(enumerate(alist)))   # 将enumerate对象转成列表以便进行分析
for item in enumerate(alist):
    print('%s: %s' % item)

for ind, val in enumerate(alist):   # 常用
    print('%s: %s' % (ind, val))

print(reversed(alist))   # 翻转
for item in reversed(alist):
    print(item)

print(sorted('hello'))   # 排序
