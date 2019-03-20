import re
from collections import Counter

def count_patt(fname, patt):
    result = Counter()
    cpatt = re.compile(patt)

    with open(fname) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                key = m.group()
                result.update([key])

    return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    ip_count = count_patt(fname, ip)
    print(ip_count)
    print('*' * 30)
    print(ip_count.most_common(5))  # 前5名

