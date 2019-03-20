
def count_pat(fname, patt):


if __name__ == '__main__':
    fname = 'access_log'
    ip = ''
    print(count_pat(fname, ip))
    br = ''
    print(count_pat(fname, br))
    fname = '/etc/passwd'
    shell = ''
    print(count_pat(fname, shell))
