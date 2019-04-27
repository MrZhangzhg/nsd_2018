import requests
import wget
import os

def has_new_ver(ver_fname, ver_url):


def has_error(fname, md5_url):


def deploy():


if __name__ == '__main__':
    # 检查是否有新版本
    app_dir = '/var/www/download/'
    ver_fname = '/var/www/deploy/live_ver'
    ver_url = 'http://192.168.4.4/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print('没有发现新版本')
        exit(1)
    # 如果有新版本，则下载
    r = requests.get(ver_url)
    ver = r.text.strip()  # 获取服务器上的版本号
    app_url = 'http://192.168.4.4/deploy/packages/myweb-%s.tar.gz' % ver
    wget.download(app_url, app_dir)
    # 校验下载的压缩包是否损坏
    app_fname = app_url.split('/')[-1]
    app_fname = os.path.join(app_dir, app_fname)  # 拼接压缩包的绝对路径
    md5_url = app_url + '.md5'  # 拼出md5值的网址
    if has_error(app_fname, md5_url):
        print('文件已损坏')
        exit(2)
    # 如果下载的文件是完好的，则部署
    deploy()
