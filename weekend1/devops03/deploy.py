"""自动部署

1. 检查最有没有新版本
2. 如果有新版本则下载下来
3. 校验下载的文件是否损坏，如果损坏则删除
4. 没有损坏则部署
/var/www/deploy/ : 存储版本文件和解压后的目录
/var/www/download/ : 存储下载的软件包
"""
import os
import wget
import requests
import hashlib
import tarfile

def has_new_ver(ver_fname, ver_url):
    "本地没有livever文件，有新版本；网上版本号大，有新版本"
    if not os.path.isfile(ver_fname):
        return True

    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    r = requests.get(ver_url)
    if r.text != local_ver:
        return True

    return False

def check_app(app_fname, md5_url):
    "文件未损坏返回True，否则是False"
    # 计算本地文件md5值
    m = hashlib.md5()
    with open(app_fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    local_md5 = m.hexdigest()

    # 取出网上md5值
    r = requests.get(md5_url)
    if local_md5 == r.text.strip():  # 比较两个md5值是否相等
        return True

    return False

def deploy(app_fname, deploy_dir):
    "将软件解压后，创建快捷方式。"
    dest = '/var/www/html/weekend1'

    # 解压
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压后目录的绝对路径
    app_path = os.path.basename(app_fname)
    app_path = app_path.replace('.tar.gz', '')
    app_path = os.path.join(deploy_dir, app_path)

    # 如果链接文件已存在，先删除，否则无法再创建
    if os.path.exists(dest):
        os.remove(dest)

    os.symlink(app_path, dest)


if __name__ == '__main__':
    deploy_dir = '/var/www/deploy'
    download_dir = '/var/www/download'
    ver_fname = os.path.join(deploy_dir, 'livever')
    ver_url = 'http://192.168.4.7/deploy/livever'

    # 判断是否有新版本，没有则退出
    if not has_new_ver(ver_fname, ver_url):
        print('未发现新版本。')
        exit(1)

    # 如果有新版本，则下载新版本软件
    r = requests.get(ver_url)
    ver = r.text.strip()
    app_url = 'http://192.168.4.7/deploy/pkgs/myweb-%s.tar.gz' % ver
    wget.download(app_url, download_dir)

    # 检查下载的压缩包是否损坏，如果已损坏则删除它
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(download_dir, app_fname)
    md5_url = app_url + '.md5'
    if not check_app(app_fname, md5_url):
        print('文件已损坏，请重试。')
        os.remove(app_fname)
        exit(2)

    # 如果软件包未损坏则部署
    deploy(app_fname, deploy_dir)

    # 更新本地版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
