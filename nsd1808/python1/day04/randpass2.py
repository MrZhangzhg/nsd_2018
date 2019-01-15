import random
import string

all_chs = string.ascii_letters + string.digits

def gen_pass(n=8):
    result = ''

    for i in range(n):
        ch = random.choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    a = gen_pass()
    print(a)
