"""
1、完全备份
(1) 压缩整个目录
(2) 计算每个文件的md5值
2、增量备份
(1) 取出前一天文件的md5值
(2) 计算当前每个文件的md5值
(3) 新增文件和有变化文件需要备份
(4) 更新md5文件
"""

from time import strftime
import os
import tarfile
import pickle
import hashlib

def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def full_backup(folder, dest, md5file):
    md5_dict = {}   # 用于保存每个文件的md5值 {'文件绝对路径': md5值}
    fname = os.path.basename(folder.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)  # 目标文件的绝对路径

    tar = tarfile.open(fname, 'w:gz')  # 压缩
    tar.add(folder)
    tar.close()

    for path, folders, files in os.walk(folder):
        for file in files:
            key = os.path.join(path, file)   # 拼出绝对路径
            md5_dict[key] = check_md5(key)   # 写入md5字典

    with open(md5file, 'wb') as fobj:   # 字典写入文件
        pickle.dump(md5_dict, fobj)

def incr_backup(folder, dest, md5file):
    fname = os.path.basename(folder.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)
    md5_dict = {}

    for path, folders, files in os.walk(folder):
        for file in files:
            key = os.path.join(path, file)
            md5_dict[key] = check_md5(key)  # 计算当前文件的md5值

    with open(md5file, 'rb') as fobj:
        oldmd5 = pickle.load(fobj)   # 取出前一天文件md5值

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dict, fobj)   # 更新文件md5值

    tar = tarfile.open(fname, 'w:gz')
    for key in md5_dict:
        if oldmd5.get(key) != md5_dict[key]:
            tar.add(key)   # 新文件、有变化文件进行备份
    tar.close()


if __name__ == '__main__':
    folder = '/tmp/demo/security/'
    dest = '/tmp/demo/'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Tue':
        full_backup(folder, dest, md5file)
    else:
        incr_backup(folder, dest, md5file)
