import hashlib
import sys
import os

def check_md5(fname):
    m = hashlib.md5()

    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    return m.hexdigest()

if __name__ == '__main__':
    try:
        fname = sys.argv[1]
    except IndexError:
        print('Usage: %s filename' % sys.argv[0])
        exit(1)   # $?的值为1
    if not os.path.isfile(fname):
        print('No such file: %s' % fname)
        exit(2)
    print(check_md5(fname))
