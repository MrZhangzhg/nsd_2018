import sys

def unix2dos(fname):
    dst_fname = fname + '.txt'

    with open(fname) as src_fobj:
        with open(dst_fname, 'w') as dst_fobj:
            for line in src_fobj:
                line = line.rstrip() + '\r\n'  # 把行尾的空白字符移除，拼接\r\n
                dst_fobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1])

# >>> with open('login4.py', 'rb') as f1:
# ...     f1.readline()
# ...
# b'import getpass\n'
# >>> with open('login4.py.txt', 'rb') as f2:
# ...     f2.readline()
# ...
# b'import getpass\r\n'

