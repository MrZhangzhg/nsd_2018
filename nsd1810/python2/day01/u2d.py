import sys

def unix2dos(fname):
    win_fname = fname + '.txt'   # 新文件名是在原有文件名后面加上.txt
    with open(fname, 'rb') as src_fobj:
        with open(win_fname, 'wb') as dst_fobj:
            for line in src_fobj:
                # 将一行文件结尾的空白字符删除，拼接上\r\n，再赋值回给line
                line = line.rstrip() + b'\r\n'
                dst_fobj.write(line)

if __name__ == '__main__':
    unix2dos(sys.argv[1])
# python3 u2d.py 文件名
