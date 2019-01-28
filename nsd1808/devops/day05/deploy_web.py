import wget
import os
import requests
import hashlib
import tarfile

def has_new_version(live_url, live_fname):
    if not os.path.isfile(live_fname):
        return True    # 如果本地没有版本文件，意味着有新版本

    with open(live_fname) as fobj:
        local_version = fobj.read()

    r = requests.get(live_url)
    if r.text != local_version:
        return True    # 本地版本和服务器版本不一样，意味着有新版本

    return False       # 如果以上判断都不成立，意味着没有新版本

def md5sum(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def deploy(app_fname, deploy_dir):
    os.chdir(deploy_dir)
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall()
    tar.close()

    app_path = os.path.basename(app_fname)   # mysite_1.0.tar.gz
    app_path = app_path.replace('.tar.gz', '')    # mysite_1.0
    app_path = os.path.join(deploy_dir, app_path)
    dest_path = '/var/www/html/nsd1808'
    if os.path.exists(dest_path):
        os.unlink(dest_path)   # 如果目标链接已存在，先删除再创建
    os.symlink(app_path, dest_path)

if __name__ == '__main__':
    live_url = 'http://192.168.4.3/deploy/live_version'
    live_fname = '/var/www/deploy/live_version'
    if not has_new_version(live_url, live_fname):
        print('没有新版本')
        exit()
    r = requests.get(live_url)
    download_dir = '/var/www/download'
    deploy_dir = '/var/www/deploy'
    app_url = 'http://192.168.4.3/deploy/packages/mysite_%s.tar.gz' % (r.text.strip())
    wget.download(app_url, download_dir)
    app_md5_url = app_url + '.md5'
    wget.download(app_md5_url, download_dir)
    if os.path.exists(live_fname):
        os.remove(live_fname)   # 如果本地有版本文件则删除，下载最新的
    wget.download(live_url, deploy_dir)
    app_fname = os.path.join(download_dir, app_url.split('/')[-1])
    local_md5 = md5sum(app_fname)
    r = requests.get(app_md5_url)
    if local_md5 != r.text.strip():
        print('文件校验失败')
        exit(1)

    deploy(app_fname, deploy_dir)
