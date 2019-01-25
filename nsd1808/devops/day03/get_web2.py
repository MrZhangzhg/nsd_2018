import re
import os
import wget
from urllib.error import HTTPError

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
    wget.download(net_url, fname)
    url_list = get_url(fname, url_patt, encoding='gbk')
    folder = '/tmp/wangyi/'   # 保存图片的本地目录
    if not os.path.exists(folder):
        os.mkdir(folder)
    for url in url_list:
        try:
            wget.download(url, folder)
        except HTTPError:
            print(url)
