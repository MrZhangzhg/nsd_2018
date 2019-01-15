'''1、所有可用的字符串
2、从所有的可用字符中随机选择一个字符
3、第2步执行N遍
4、把取出的所有的字符拼接起来
'''
import random

all_chs = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
result = ''

for i in range(8):
    ch = random.choice(all_chs)
    result += ch

print(result)
