from urllib import request
import re
import os

def download(url, fname):
    r = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = r.read(1024)
            if not data:
                break
            fobj.write(data)

def get_url(fname, patt, encoding=None):
    cpatt = re.compile(patt)
    url_list = []
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                url_list.append(m.group())
    return url_list

if __name__ == '__main__':
    net_url = 'http://www.163.com/'
    net_fname = '/tmp/163.html'
    download(net_url, net_fname) # 下载网易首页文件
    img_patt = '(http|https)://[-\w/.]+\.(jpg|gif|png|jpeg)'
    img_url = get_url(net_fname, img_patt, 'gbk')  # 所有图片网址
    # 创建目标目录
    img_dir = '/tmp/net163/'
    if not os.path.isdir(img_dir):
        os.mkdir(img_dir)
    # 下载图片
    for url in img_url:
        fname = url.split('/')[-1]  # 从URL中切出文件名
        fname = os.path.join(img_dir, fname)  # 拼接绝对路径
        download(url, fname)
