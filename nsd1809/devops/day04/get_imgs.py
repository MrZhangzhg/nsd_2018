from urllib import request
import os
import re

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_urls(fname, patt, encoding='utf8'):
    patt_list = []
    cpatt = re.compile(patt)
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())

    return patt_list


if __name__ == '__main__':
    path = '/tmp/myimg'
    url_163 = 'http://www.163.com'
    if not os.path.exists(path):
        os.mkdir(path)
    fname_163 = os.path.join(path, '163.html')
    download(url_163, fname_163)  # 下载网易首页
    ##############################
    img_patt = '(http|https)://[-/.\w]+\.(png|jpg|jpeg|gif)'
    img_list = get_urls(fname_163, img_patt, encoding='gbk')
    print(img_list)
    ##############################

