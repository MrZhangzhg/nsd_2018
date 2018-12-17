import re

def count_patt(fname, patt):
    cpatt = re.compile(patt)
    patt_dict = {}
    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                patt_dict[key] = patt_dict.get(key, 0) + 1
    return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 192.168.1.10 | 1234.45678.22.12336788
    br = 'Chrome|Firefox|MSIE'
    print(count_patt(fname, ip))
    print(count_patt(fname, br))
