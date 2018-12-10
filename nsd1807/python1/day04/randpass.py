import random

all_chs = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLXCVBNM1234567890'
result = ''

for i in range(8):
    ch = random.choice(all_chs)
    result += ch

print(result)
