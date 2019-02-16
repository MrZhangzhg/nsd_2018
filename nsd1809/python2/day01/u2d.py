import sys

def unix2dos(fname):
    dst_fname = fname + '.txt'   # 新文件名是原文件尾部加上.txt后缀
    with open(fname) as src_fobj:
        with open(dst_fname, 'w') as dst_fobj:
            for line in src_fobj:
                # 把原文件结尾的\n\r组合全部消除，再加上\r\n
                line = line.rstrip('\n\r') + '\r\n'
                dst_fobj.write(line)  # 写入新文件

if __name__ == '__main__':
    unix2dos(sys.argv[1])   # 文件名使用位置参数接收
