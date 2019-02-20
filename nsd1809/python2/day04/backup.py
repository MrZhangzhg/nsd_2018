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

def full_backup(src, dest, md5file):
    "需要把包整个文件，并且计算每个文件的md5值"
    fname = os.path.basename(src.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5_dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            full_path = os.path.join(path, file)
            md5_dict[full_path] = check_md5(full_path)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dict, fobj)

def incr_backup(src, dest, md5file):
    """
    计算当前的md5值
    取出前一天的md5值
    判断哪些文件是新增的，哪些文件是改动的，这样的文件才要备份
    """
    fname = os.path.basename(src.rstrip('/'))
    fname = '%s_incr_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    with open(md5file, 'rb') as fobj:  # 取出前一天的md5值
        old_md5 = pickle.load(fobj)

    new_md5 = {}  # 计算当前提md5值
    for path, folders, files in os.walk(src):
        for file in files:
            full_path = os.path.join(path, file)
            new_md5[full_path] = check_md5(full_path)

    tar = tarfile.open(fname, 'w:gz')
    for key in new_md5:
        # if key not in old_md5 or new_md5[key] != old_md5[key]:
        if old_md5.get(key) != new_md5[key]:
            tar.add(key)
    tar.close()

    with open(md5file, 'wb') as fobj:  # 把新md5值写入文件
        pickle.dump(new_md5, fobj)

if __name__ == '__main__':
    src = '/tmp/mydemo/security/'
    dest = '/tmp/mydemo/'
    md5file = '/tmp/mydemo/md5.data'
    if strftime('%a') == 'Mon':  # 如果是周一则进行完全备份
        full_backup(src, dest, md5file)
    else:
        incr_backup(src, dest, md5file)  # 其他时间增量备份
