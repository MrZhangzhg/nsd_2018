import re

class CountPatt:
    def count_patt(self, fname, patt):
        patt_dict = {}
        cpatt = re.compile(patt)
        with open(fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    patt_dict[key] = patt_dict.get(key, 0) + 1
        return patt_dict

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'
    cp = CountPatt()
    print(cp.count_patt(fname, ip))
