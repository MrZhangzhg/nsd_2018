import re

def count_pat(fname, patt):
    result = {}
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result[key] = result.get(key, 0) + 1

    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1.11.111.25   1234.56789.1.235
    print(count_pat(fname, ip))
    br = 'Chrome|Firefox|MSIE'
    print(count_pat(fname, br))
    fname = '/etc/passwd'
    shell = 'bash$|nologin$'
    print(count_pat(fname, shell))
