import sys
import hashlib

def check_md5(fname):
    m = hashlib.md5()   # 创建md5对象
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)  # 每次读取4K内容，更新到md5对象
    return m.hexdigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))
