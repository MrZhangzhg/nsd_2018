import os
import requests


def has_new_version(local_ver, ver_url):
    if not os.path.isfile(local_ver):
        return True  # 本地没有版本文件，意味道着有新版本

    with open(local_ver) as fobj:
        lver = fobj.read()   # 读取本地版本文件中的版本号
    r = requests.get(ver_url)
    if lver != r.text:
        return True   # 网上的版本号和本地版本号不同，意味道着有新版本

    return False   # 以上判断全失败，意味着没有新版本

if __name__ == '__main__':
    local_ver = '/var/www/deploy/live_version'
    ver_url = 'http://192.168.4.4/deploy/live_version'
    if not has_new_version(local_ver, ver_url):
        print('没有发现新版本')
        exit()
