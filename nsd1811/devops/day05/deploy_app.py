import requests
import wget
import os
import hashlib
import tarfile

def has_new_ver(ver_fname, ver_url):
    # 如果本地没有版本文件，表示有新版本
    if not os.path.isfile(ver_fname):
        return True

    # 读取本地版本文件内容
    with open(ver_fname) as fobj:
        local_ver = fobj.read()

    # 获取远程版本
    r = requests.get(ver_url)
    remote_ver = r.text

    # 如果本地和远程版本不一样，表示有新版本
    if local_ver != remote_ver:
        return True

    # 如果本地和远程版本一样，则没有新版本
    return False

def has_error(fname, md5_url):
    # 计算本地文件的md5
    m = hashlib.md5()
    with open(fname, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    r = requests.get(md5_url)  # 取出服务器公布的md5值
    if m.hexdigest() == r.text.strip():
        return False  # 如果两个md5值相等，表示文件未损坏

    return True

def deploy(app_fname):
    # app_fname: /var/www/download/myweb-1.0.tar.gz
    # 解压缩
    deploy_dir = '/var/www/deploy/'
    tar = tarfile.open(app_fname, 'r:gz')
    tar.extractall(path=deploy_dir)
    tar.close()
    # 拼出解压目录的绝对路径
    app_path = os.path.basename(app_fname)   # myweb-1.0.tar.gz
    app_path = app_path.replace('.tar.gz', '')  # myweb-1.0
    app_path = os.path.join(deploy_dir, app_path)
    # 创建链接，如果链接已存在，先删除它
    link = '/var/www/html/nsd1811'
    if os.path.exists(link):
        os.remove(link)
    os.symlink(app_path, link)

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
        os.remove(app_fname)  # 如果文件已扣坏，则删除它
        exit(2)
    # 如果下载的文件是完好的，则部署
    deploy(app_fname)
    # 更新本地版本文件
    with open(ver_fname, 'w') as fobj:
        fobj.write(r.text)
