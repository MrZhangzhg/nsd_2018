import re
from collections import Counter

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        patt_counter = Counter()
        cpatt = re.compile(patt)
        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    patt_counter.update([m.group()])
        return patt_counter

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    br = 'Chrome|Firefox|MSIE'
    cp = CountPatt(fname)
    print(cp.count_patt(ip))
    print(cp.count_patt(br))
