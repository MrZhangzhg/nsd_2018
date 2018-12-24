import os
import requests
import wget
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


def deploy_web():


if __name__ == '__main__':
    live_ver_url = 'http://192.168.4.3/deploy/live_version'
    local_ver_path = '/var/www/download/live_version'
    r = requests.get(live_ver_url)
    live_ver = r.text.strip()  # 获取最新软件的版本号
    live_app_url = 'http://192.168.4.3/deploy/packages/webapp_%s.tar.gz' % live_ver
    local_app_path = '/var/www/download/webapp_%s.tar.gz' % live_ver
    live_md5_url = 'http://192.168.4.3/deploy/packages/webapp_%s.tar.gz.md5' % live_ver
    if not os.path.exists(local_ver_path):
        wget.download(live_app_url, local_app_path)
        local_md5 = check_md5(local_app_path)  # 计算下载下来的软件md5值
        r = requests.get(live_md5_url)
        live_md5 = r.text.strip()   # 获取jenkins服务器上的md5值
        if local_md5 != live_md5:
            print('文件在下载过程中已损坏')
            exit(1)
        deploy_web()
    elif '本地版本旧':
        '部署软件'
