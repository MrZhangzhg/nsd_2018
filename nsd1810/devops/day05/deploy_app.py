"""
has_new_ver: 用于检查是否有新版本
check_app: 用于检查下载的软件包是否损坏
deploy: 用于部署应用程序
"""
import os
import requests


def has_new_ver(ver_url, ver_fname):
    if not os.path.isfile(ver_fname):
        return True  # 如果本地没有版本文件，则认为有新版本的软件

    with open(ver_fname) as fobj:
        app_ver = fobj.read()

    r = requests.get(ver_url)
    if app_ver != r.text:
        return True   # 网上版本和本地版本不一样，意味着有新版本

    return False   # 网上版本和本地版本一样，则没有新版本

def check_app():


def deploy():


if __name__ == '__main__':
    ver_url = 'http://192.168.4.4/deploy/livever'
    ver_fname = '/var/www/deploy/livever'
    if not has_new_ver(ver_url, ver_fname):
        print('没有发现新版本')
        exit()
