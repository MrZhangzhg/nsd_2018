import os
import tarfile
import pickle
import hashlib
from time import strftime

def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def full_backup(src_dir, dst_dir, md5file):
    # 构建备份文件的绝对路径
    fname = '%s_full_%s.tar.gz' %\
            (os.path.basename(src_dir.rstrip('/')), strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    # 将源目录打包压缩
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将md5字典写入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src_dir, dst_dir, md5file):
    pass

if __name__ == '__main__':
    src_dir = '/tmp/mydemo/security/'
    dst_dir = '/tmp/demo/'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') != 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
