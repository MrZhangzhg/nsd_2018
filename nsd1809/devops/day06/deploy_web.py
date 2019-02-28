import os
import requests
import wget
import hashlib
import tarfile


def has_new_version(local_ver, ver_url):
    if not os.path.isfile(local_ver):
        return True  # 本地没有版本文件，意味道着有新版本

    with open(local_ver) as fobj:
        lver = fobj.read()   # 读取本地版本文件中的版本号
    r = requests.get(ver_url)
    if lver != r.text:
        return True   # 网上的版本号和本地版本号不同，意味道着有新版本

    return False   # 以上判断全失败，意味着没有新版本

def check_md5(fname):
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
    app_path = os.path.basename(app_fname)  # myweb-1.0.tar.gz
    app_path = app_path.replace('.tar.gz', '')  # myweb-1.0
    app_path = os.path.join(deploy_dir, app_path)  # /var/www/deploy/myweb-1.0
    link = '/var/www/html/nsd1809'
    # 如果链接已存在，先删除，因为不能创建一个链接，覆盖已存在的
    if os.path.exists(link):
        os.unlink(link)
    os.symlink(app_path, link)


if __name__ == '__main__':
    local_ver = '/var/www/deploy/live_version'
    ver_url = 'http://192.168.4.4/deploy/live_version'
    if not has_new_version(local_ver, ver_url):
        print('没有发现新版本')
        exit()
    # 如果有新版本，下载最新版本的软件和它的md5值文件
    r = requests.get(ver_url)
    ver_num = r.text.strip()
    app_url = 'http://192.168.4.4/deploy/packages/myweb-%s.tar.gz' % ver_num
    app_md5_url = app_url + '.md5'
    download_dir = '/var/www/download'
    wget.download(app_url, download_dir)
    # wget.download(app_md5_url, download_dir)
    # 校验下载的文件是否损坏，如果损坏则退出
    app_fname = app_url.split('/')[-1]  # myweb-1.0.tar.gz
    app_fname = os.path.join(download_dir, app_fname)  # /var/www/download/myweb-1.0.tar.gz
    app_md5 = check_md5(app_fname)
    r = requests.get(app_md5_url)
    if app_md5 != r.text.strip():
        print('文件校验失败')
        exit(1)  # 如果下载的文件md5值与网上提供的不一致，则退出
    # 部署
    deploy_dir = '/var/www/deploy/'
    live_fname = os.path.join(deploy_dir, 'live_version')
    # 如果本地已经有live_version文件，先删除，否则下载的时候，不会覆盖
    if os.path.exists(live_fname):
        os.remove(live_fname)
    wget.download(ver_url, deploy_dir)
    deploy(app_fname, deploy_dir)


