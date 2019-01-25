import re
import os
import urllib.error
from urllib import request

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def get_url(fname, patt, encoding=None):
    url_list = []
    cpatt = re.compile(patt)
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            for m in cpatt.finditer(line):    # [匹配对象，匹配对象]
                url_list.append(m.group())
    return url_list

if __name__ == '__main__':
    net_url = 'http://www.163.com/'
    fname = '/tmp/163.html'
    url_patt = '(http|https)://[-\w./]+\.(png|jpg|jpeg|gif)'
    download(net_url, fname)
    url_list = get_url(fname, url_patt, encoding='gbk')
    folder = '/tmp/wangyi/'
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in url_list:
        fname = url.split('/')[-1]
        fname = os.path.join(folder, fname)
        try:
            download(url, fname)
        except urllib.error.HTTPError:
            print(url)
