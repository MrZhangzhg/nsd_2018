# print("Tom's pet is a cat")
# print('Tom said"Hello World"')
words = 'Hello\nworld\ntom\njerry'
# lines = '''1st line.
# 2nd line.
# 3rd line.'''
# print(words)
# print(lines)

if 'tom' in words:
    print('yes')

if 'tom' not in words:
    print('not in')
else:
    print('tom in words')

if -0.0:
    print('ok')        # 任何值为0的数字都是False，非0为True

if -0.01:
    print('0.01 is ok')

if ' ':                # 任何非空对象都是True，空为False
    print('space is true')

if '':
    print('空字符串是False')

if not []:
    print('空列表也是False')

if not None:
    print('None也是False，表示空')


