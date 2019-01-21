import re

def count_patt(fname, patt):
    patt_dict = {}
    cpatt = re.compile(patt)   # 将模式编译
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)  # 在一行中匹配模式
            if m:   # 如果匹配到了为真(没匹配到是None，None为假)
                key = m.group()   # 取出匹配的内容
                # 模式没在字典中，get返回值是0，否则是字典中的值
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1234.1.23.209886  1.23.123.10
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
