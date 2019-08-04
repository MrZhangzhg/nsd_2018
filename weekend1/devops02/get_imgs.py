import wget
import re
import os
from urllib import error

web_url = 'http://www.163.com'
web_dir = '/tmp/163'
web_index = '/tmp/163/163.html'
img_patt = '(https|http)://[-./\w]+\.(jpg|jpeg|png|gif)'
img_list = []

# 创建保存图片的目录
if not os.path.exists(web_dir):
    os.mkdir(web_dir)
# 下载网易的首页
if not os.path.exists(web_index):
    wget.download(web_url, web_index)

# 获取网易首页中所有的图片url
# 注意，网易的页面，字符编码是gbk，而不是默认的utf8
cpatt = re.compile(img_patt)
with open(web_index, encoding='gbk') as fobj:
    for line in fobj:
        m = cpatt.search(line)
        if m:
            img_list.append(m.group())

# print(img_list)
for img_url in img_list:
    try:
        wget.download(img_url, web_dir)
    except error.HTTPError:
        pass



