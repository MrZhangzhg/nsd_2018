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

def get_patt(fname, patt, encoding='utf8'):
    cpatt = re.compile(patt)
    patt_list = []
    with open(fname, encoding=encoding) as fobj:
        for line in fobj:
            m = cpatt.search(line)
            if m:
                patt_list.append(m.group())
    return patt_list

if __name__ == '__main__':
    url163 = 'http://www.163.com'
    fname163 = '/tmp/163.html'
    download(url163, fname163)
    img_patt = 'http://[\w/.-]+\.(jpg|png|jpeg|gif)'
    img_urls = get_patt(fname163, img_patt, 'gbk')
    print(img_urls)
