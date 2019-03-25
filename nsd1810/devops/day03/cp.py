from tqdm import tqdm
import sys
import os

def copy(src_fname, dst_fname):
    # 计算出拷贝文件需要循环的次数
    buf = 4096
    size = os.stat(src_fname).st_size
    counter, extra = divmod(size, buf)
    if extra:  # 如果extra不是0，将计数器加1
        counter += 1

    with open(src_fname, 'rb') as src_fobj:
        with open(dst_fname, 'wb') as dst_fobj:
            for i in tqdm(range(counter)):
                data = src_fobj.read(buf)
                dst_fobj.write(data)

if __name__ == '__main__':
    copy(sys.argv[1], sys.argv[2])
