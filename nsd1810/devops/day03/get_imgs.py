from urllib import request
import re

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
    download(net_url, net_fname)
    img_patt = '(http|https)://[-\w/.]+\.(jpg|gif|png|jpeg)'
    print(get_url(net_fname, img_patt, 'gbk'))

