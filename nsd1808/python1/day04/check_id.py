import sys
import keyword
import string

first_chs = string.ascii_letters + '_'
other_chs = first_chs + string.digits

def check_id(idt):   # idt = 'abc@123'
    if keyword.iskeyword(idt):
        return '%s是关键字' % idt   # 遇到return, 函数结束

    if idt[0] not in first_chs:
        return '首字符不合法'

    for ind, ch in enumerate(idt[1:]):   # enumerate('bc@123')
        if ch not in other_chs:
            return '第%s个字符不合法' % (ind + 2)   # 遇到return, 函数结束

    return '%s是合法的' % idt

if __name__ == '__main__':
    result = check_id(sys.argv[1])
    print(result)
