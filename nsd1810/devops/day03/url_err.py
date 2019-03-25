from urllib import request, error

url1 = 'http://127.0.0.1/abc/'
url2 = 'http://127.0.0.1/ban/'

try:
    r1 = request.urlopen(url1)
except error.HTTPError as e:
    print('出错啦：', e)

try:
    r2 = request.urlopen(url2)
except error.HTTPError as e:
    print('出错啦：', e)
