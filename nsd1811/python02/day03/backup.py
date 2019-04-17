import os
import tarfile
from check_md5 import check_md5
from time import strftime

def full_backup(src, dst, md5file):
    fname = os.path.basename(src)
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    tar = tarfile.open(fname, 'w:gz')
    tar.add(src)
    tar.close()

    md5dict = {}


def incr_backup(src, dst, md5file):


if __name__ == '__main__':
    src = '/tmp/mydemo/security'
    dst = '/tmp/demo'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(src, dst, md5file)
    else:
        incr_backup(src, dst, md5file)
