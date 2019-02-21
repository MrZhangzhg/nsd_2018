import re

def count_patt(fname, patt):
    cpatt = re.compile(patt)  # 编译模式，提升效率
    patt_dict = {}
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:  # 如果匹配到了，返回的是匹配对象，非空即为真，没匹配到是None，None是假
                key = m.group()
                # if key not in patt_dict:
                #     patt_dict[key] = 1
                # else:
                #     patt_dict[key] += 1
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'   # 1.10.125.3, 1000.12345.23.1234567
    print(count_patt(fname, ip))
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, br))
    print(count_patt('/etc/passwd', 'bash$|nologin$'))
