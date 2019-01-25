import re
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
    

if __name__ == '__main__':
    net_url = 'http://www.163.com/'
    fname = '/tmp/163.html'
    url_patt = '(http|https)://[\w.-/]+\.(png|jpg|jpeg|gif)'
    download(net_url, fname)
    url_list = get_url(fname, url_patt, encoding='gbk')
