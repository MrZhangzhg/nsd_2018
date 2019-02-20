import os
import tarfile
from time import strftime

def full_backup(src, dest, md5file):
    "需要把包整个文件，并且计算每个文件的md5值"
    fname = os.path.basename(src.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

def incr_backup(src, dest, md5file):
    pass

if __name__ == '__main__':
    src = '/tmp/mydemo/security/'
    dest = '/tmp/mydemo/'
    md5file = '/tmp/md5.data'
    if strftime('%a') != 'Mon':  # 如果是周一则进行完全备份
        full_backup(src, dest, md5file)
    else:
        incr_backup(src, dest, md5file)  # 其他时间增量备份
