import re
import os
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
    result = []  # 把所有的匹配存入该列表
    with open(fname, encoding=code) as fobj:  # 打开文件时，可以指定字符集
        for line in fobj:
            match_objs = cpatt.finditer(line)  # 找到一行中的多个模式
            for m in match_objs:
                result.append(m.group())  # 将找到的内容追加到列表
    return result


if __name__ == '__main__':
    net163 = 'http://www.163.com'
    file163 = '/tmp/163.html'
    download(net163, file163)  # 下载网易首页
    # 编写图片url的正则表达式
    img_patt = '(http|https)://[-\w./]+(\.jpg|\.jpeg|\.png|\.gif)'
    img_list = find_patt(file163, img_patt, 'gbk')  # 获取所有的图片URL
    # print(img_list)
    img_dir = '/tmp/images/'
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)

    for img_url in img_list:
        fname = img_url.split('/')[-1]
        fname = os.path.join(img_dir, fname)
        download(img_url, fname)
