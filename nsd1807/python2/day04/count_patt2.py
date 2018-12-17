import re
from collections import Counter

class CountPatt:
    def __init__(self, patt):
        self.cpatt = re.compile(patt)

    def count_patt(self, fname):
        result = Counter()
        with open(fname) as fobj:
            for line in fobj:
                m = self.cpatt.search(line)
                if m:
                    key = m.group()
                    result.update([key])
        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = CountPatt(ip)
    a = cp.count_patt(fname)
    print(a)
    print(a.most_common(3))
