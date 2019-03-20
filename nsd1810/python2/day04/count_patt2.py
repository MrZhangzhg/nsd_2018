import re

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_patt(self, patt):
        result = {}
        cpatt = re.compile(patt)

        with open(self.fname) as fobj:
            for line in fobj:
                m = cpatt.search(line)
                if m:
                    key = m.group()
                    result[key] = result.get(key, 0) + 1

        return result

if __name__ == '__main__':
    fname = 'access_log'
    ip = '^(\d+\.){3}\d+'  # 1.11.111.25   1234.56789.1.235
    br = 'Chrome|Firefox|MSIE'
    cp1 = CountPatt(fname)
    print(cp1.count_patt(ip))
    print(cp1.count_patt(br))

    passwd_fname = '/etc/passwd'
    cp2 = CountPatt(passwd_fname)
    shell = 'bash$|nologin$'
    print(cp2.count_patt(shell))
