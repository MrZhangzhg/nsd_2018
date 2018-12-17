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
    md5_dict = {}
    fname = os.path.basename(folder.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname, strftime('%Y%m%d'))
    fname = os.path.join(dest, fname)

    tar = tarfile.open(fname, 'w:gz')
    tar.add(folder)
    tar.close()

    for path, folders, files in os.walk(folder):
        for file in files:
            md5_dict[file] = check_md5(file)

    with open(md5file, 'wb') as fobj:
        pickle.dump(md5_dict, fobj)

def incr_backup(folder, dest, md5file):


if __name__ == '__main__':
    folder = '/tmp/demo/security/'
    dest = '/tmp/demo/'
    md5file = '/tmp/demo/md5.data'
    if strftime('%a') == 'Mon':
        full_backup(folder, dest, md5file)
    else:
        incr_backup(folder, dest, md5file)
