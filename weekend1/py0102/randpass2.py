from random import choice
from string import ascii_letters, digits

# 全局变量从定义开始到程序结束，任何位置都可见可用
all_chs = ascii_letters + digits

def gen_pass(n=8):
    # 函数内部的变量是局部变量，只能在函数内使用
    result = ''

    for i in range(n):
        ch = choice(all_chs)
        result += ch

    return result

if __name__ == '__main__':
    print(gen_pass())
    print(gen_pass(4))
