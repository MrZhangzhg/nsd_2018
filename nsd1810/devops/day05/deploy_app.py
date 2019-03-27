"""
has_new_ver: 用于检查是否有新版本
check_app: 用于检查下载的软件包是否损坏
deploy: 用于部署应用程序
"""
import os
import requests
import wget
import hashlib
import tarfile

def has_new_ver(ver_url, ver_fname):
    if not os.path.isfile(ver_fname):
        return True  # 如果本地没有版本文件，则认为有新版本的软件

    with open(ver_fname) as fobj:
        app_ver = fobj.read()

    r = requests.get(ver_url)
    if app_ver != r.text:
        return True   # 网上版本和本地版本不一样，意味着有新版本

    return False   # 网上版本和本地版本一样，则没有新版本

def check_app(app_fname, app_md5_url):
    r = requests.get(app_md5_url)
    remote_md5 = r.text.strip()  # 取出网上公布的md5值

    # 计算本地文件的md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)

    if remote_md5 == m.hexdigest():  # 如果本地和网上的md5值一样，则文件未损坏
        return True

    return False

def deploy(app_fname):
    deploy_dir = '/var/www/deploy'
    # 解压文件到deploy目录
    os.chdir(deploy_dir)
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall()
    tar.close()

    # 拼接出解压后目录的绝对路径
    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz', '')
    app_path = os.path.join(deploy_dir, app_path)

    # 创建链接
    link = '/var/www/html/nsd1810'
    if os.path.exists(link):
        os.unlink(link)  # 如果有链接到老版本的链接，先删除
    os.symlink(app_path, link)

if __name__ == '__main__':
    ver_url = 'http://192.168.4.4/deploy/livever'
    ver_fname = '/var/www/deploy/livever'
    if not has_new_ver(ver_url, ver_fname):
        print('没有发现新版本')
        exit()

    # 有新版本，则下载最新的软件包
    r = requests.get(ver_url)
    app_ver = r.text.strip()  # 把版本字符串结尾的\n去除
    app_url = 'http://192.168.4.4/deploy/packages/myweb-%s.tar.gz' % app_ver
    download_dir = '/var/www/download'
    wget.download(app_url, download_dir)

    # 检查下载的文件是否损坏，本地文件算出的md5值，如果和网上提供的不一样，则损坏
    app_fname = '/var/www/download/myweb-%s.tar.gz' % app_ver
    app_md5_url = app_url + '.md5'
    if not check_app(app_fname, app_md5_url):
        print('下载的文件校验失败')
        exit(1)

    # 如果下载的软件未损坏，则更新本地版本文件
    with open(ver_fname, 'w') as fobj:   # 更新本地版本文件
        fobj.write(r.text)

    deploy(app_fname)  # 部署软件
