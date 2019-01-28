import wget
import os
import requests

def has_new_version(live_url, live_fname):
    if not os.path.isfile(live_fname):
        return True    # 如果本地没有版本文件，意味着有新版本

    with open(live_fname) as fobj:
        local_version = fobj.read()

    r = requests.get(live_url)
    if r.text != local_version:
        return True    # 本地版本和服务器版本不一样，意味着有新版本

    return False       # 如果以上判断都不成立，意味着没有新版本

def md5sum():
    pass

def deploy():
    pass

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
    wget.download(live_url, deploy_dir)
