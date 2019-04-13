import sys
import keyword
from string import ascii_letters, digits

first_chs = ascii_letters + '_'
other_chs = first_chs + digits

def check_idt(idt):   # abc@123
    if keyword.iskeyword(idt):
        return '%s 是关键字' % idt

    if not idt[0] in first_chs:
        return '第1个字符不合法'

    for ind, ch in enumerate(idt[1:]):  # [(0, 'b'), (1, 'c'), (2, '@'), (3, '1'), (4, '2'), (5, '3')]
        if ch not in other_chs:
            return "第%s个字符不合法" % (ind + 2)

    return '%s是合法的标识符' % idt

if __name__ == '__main__':
    print(check_idt(sys.argv[1]))
