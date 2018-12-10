import keyword
import string

first_chs = string.ascii_letters + '_'
other_chs = first_chs + string.digits

def check_id(idt):
    '函数即使有多个return，也只会执行一个。函数也就结束了'
    if keyword.iskeyword(idt):
        return '%s是关键字' % idt

    if idt[0] not in first_chs:
        return '首字符不合法'

    for ind, ch in enumerate(idt[1:]):
        if ch not in other_chs:
            return '第%s个字符不合法' % (ind + 2)

    return '%s是合法的标识符' % idt

if __name__ == '__main__':
    idt = input('请输入字行串: ')
    print(check_id(idt))
