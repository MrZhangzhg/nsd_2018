import os
import tarfile
import pickle
from check_md5 import check_md5
from time import strftime

def full_backup(src, dst, md5file):
    # 生成压缩包的绝对路径
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)  # 拼接绝对路径

    # 打包文件
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 将字典写入文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incr_backup(src, dst, md5file):
    # 生成压缩包的绝对路径
    fname = os.path.basename(src)
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)

    # 计算每个文件的md5值
    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    # 取出前一天的md5字典
    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    # 更新md5字典文件
    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

    # 从新字典取出文件名(key)和md5值，和老字典比较，新增的和修改过的需要打包
    tar = tarfile.open(fname, 'w:gz')
    for key in md5dict:
        if md5dict[key] != old_md5.get(key):
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src = '/tmp/mydemo/security'
    dst = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
