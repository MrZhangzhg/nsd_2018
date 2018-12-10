hi = 'hello'
alist = [10, 200, 30, 40, 15, 35]

for ind in range(len(hi)):
    print(ind, hi[ind])

# print(list(enumerate(alist)))
for item in enumerate(alist):
    print(item)

for ind, val in enumerate(alist):
    print(ind, val)

print(list(reversed(alist)))   # 翻转
for i in reversed(alist):
    print(i)

print(sorted(alist))           # 排序
