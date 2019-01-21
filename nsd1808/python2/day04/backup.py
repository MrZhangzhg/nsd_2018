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
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = "%s_full_%s.tar.gz" % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(src_dir)
    tar.close()

    md5dict = {}
    for path, folers, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            md5dict[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5dict, fobj)

def incr_backup(src_dir, dst_dir, md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = "%s_incr_%s.tar.gz" % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dst_dir, fname)

    with open(md5file, 'rb') as fobj:
        old_md5 = pickle.load(fobj)

    cur_md5 = {}
    for path, folers, files in os.walk(src_dir):
        for file in files:
            key = os.path.join(path, file)
            cur_md5[key] = check_md5(key)

    with open(md5file, 'wb') as fobj:
        pickle.dump(cur_md5, fobj)

    tar = tarfile.open(fname, 'w:gz')
    for key in cur_md5:
        if old_md5.get(key) != cur_md5[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/tmp/demo'
    md5file = '/tmp/md5.data'
    if strftime('%a') != 'Mon':
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)
