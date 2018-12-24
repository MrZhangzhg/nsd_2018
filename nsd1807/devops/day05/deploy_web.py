import os
import requests
import wget
import hashlib
import tarfile

def has_new_version(local_ver_path, live_ver_url):
    if not os.path.isfile(local_ver_path):
        return True   # 本地不存在版本文件，表明有新版本

    r = requests.get(live_ver_url)
    server_ver = r.text   # 获取服务器上版本
    with open(local_ver_path) as fobj:
        local_ver = fobj.read()   # 获取本地版本
    if server_ver != local_ver:
        return True

    return False


def check_md5(fname):
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()


def deploy_web(local_app_path):
    web_link = '/var/www/html/nsd1807'
    deploy_dir = '/var/www/deploy/'
    os.chdir(deploy_dir)
    tar = tarfile.open(local_app_path, 'r:gz')
    tar.extractall()
    tar.close()
    app_fname = os.path.basename(local_app_path)  # webapp_1.0.tar.gz
    # 拼出/var/www/deploy/webapp_x.x
    deploy_path = os.path.join(deploy_dir, app_fname.replace('.tar.gz', ''))
    if os.path.exists(web_link):   # 链接已存在先删除，否则创建链接时报错
        os.unlink(web_link)
    os.symlink(deploy_path, web_link)  # 创建软链接

if __name__ == '__main__':
    live_ver_url = 'http://192.168.4.3/deploy/live_version'
    local_ver_path = '/var/www/download/live_version'
    r = requests.get(live_ver_url)
    live_ver = r.text.strip()  # 获取最新软件的版本号
    live_app_url = 'http://192.168.4.3/deploy/packages/webapp_%s.tar.gz' % live_ver
    local_app_path = '/var/www/download/webapp_%s.tar.gz' % live_ver
    live_md5_url = 'http://192.168.4.3/deploy/packages/webapp_%s.tar.gz.md5' % live_ver

    if not has_new_version(local_ver_path, live_ver_url):
        print('没有发现新版本')
        exit(1)

    # 如果有新版本则向下执行
    wget.download(live_app_url, local_app_path)
    local_md5 = check_md5(local_app_path)  # 计算下载下来的软件md5值
    r = requests.get(live_md5_url)
    live_md5 = r.text.strip()   # 获取jenkins服务器上的md5值
    if local_md5 != live_md5:
        print('文件在下载过程中已损坏')
        exit(2)

    # 如果下载的文件没有损坏，则部署
    deploy_web(local_app_path)
    wget.download(live_ver_url, local_ver_path)   # 部署成功后，更新本地版本文件
