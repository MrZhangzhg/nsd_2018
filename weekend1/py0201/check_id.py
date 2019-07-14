import sys
import keyword
from string import ascii_letters, digits

first_chs = ascii_letters + '_'
other_chs = first_chs + digits

def check_id(idt):
    # 函数可以有多个return，但是只有一个能执行。遇到return函数就结束了
    if idt in keyword.kwlist:
        return '%s是关键字' % idt

    if idt[0] not in first_chs:
        return '首字符不合法'

    for ind, ch in enumerate(idt[1:]):   # abc@123#
        if ch not in other_chs:
            return '第%s位置的字符不合法' % (ind + 2)

    return '%s是合法的标识符' % idt

if __name__ == '__main__':
    print(check_id(sys.argv[1]))
