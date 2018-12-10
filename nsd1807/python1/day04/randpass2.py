import random
import string

all_chs = string.ascii_letters + string.digits

def randpass(n=8):
    result = ''

    for i in range(n):
        ch = random.choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    a = randpass()
    print(a)
    print(randpass(4))
