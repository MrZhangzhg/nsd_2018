import re
from urllib.request import urlopen


def download(url, fname):
    html = urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

def find_patt(fname, patt, code='utf8'):
    cpatt = re.compile(patt)
    result = []
    with open(fname, encoding=code) as fobj:
        for line in fobj:
            match_objs = cpatt.finditer(line)
            for m in match_objs:
                result.append(m.group())
    return result


if __name__ == '__main__':
    net163 = 'http://www.163.com'
    file163 = '/tmp/163.html'
    download(net163, file163)
    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png|\.gif)'
    img_list = find_patt(file163, img_patt, 'gbk')
    print(img_list)


