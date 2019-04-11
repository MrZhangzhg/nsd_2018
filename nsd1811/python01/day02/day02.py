if 3 > 0:
    print('3>0, yes')
    print('3>0, ok')

print('*' * 40)

if 'th' in 'python':
    print('th in python, yes')

print('*' * 40)

if -0.0:    # 任何值为0的数字都是False
    print('yes')

print('*' * 40)

if 30:
    print('非0数字，true')

print('*' * 40)

if ' ':
    print('任何非空字符都是true，空格也是一个字符')

print('*' * 40)

if '':   # 空字符串
    print('yes')

if [False]:
    print('非空列表，true')

print('*' * 40)

if []:   # 空列表为False
    print('ok')
else:
    print('空列表，False')
