import os
import tarfile
import pickle
from check_md5 import check_md5
from time import strftime

def full_backup(src, dst, md5file):
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)  # 拼接绝对路径

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}
    for path, folders, files in os.walk(src):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)


def incr_backup(src, dst, md5file):
    pass

if __name__ == '__main__':
    src = '/tmp/mydemo/security'
    dst = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') != 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
