import sys
import keyword
import string

first_chs = string.ascii_letters + '_'
other_chs = first_chs + string.digits

def check_idt(idt):
    if keyword.iskeyword(idt):    # idt -> abc@123
        return '%s是关键字' % idt

    if idt[0] not in first_chs:   # 'a' not in first_chs
        return '第1个字符不合法'

    for ind, ch in enumerate(idt[1:]):   # idt[1:] -> bc@123
        if ch not in other_chs:
            return '第%s个字符不合法' % (ind + 2)

    return '%s是合法的标识符' % idt


if __name__ == '__main__':
    print(check_idt(sys.argv[1]))
# check_idt.py abc@123
