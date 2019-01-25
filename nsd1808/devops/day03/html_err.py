from urllib import request
from urllib.error import HTTPError

url1 = 'http://127.0.0.1/abc/'
url2 = 'http://127.0.0.1/ban/'

for url in [url1, url2]:
    try:
        html = request.urlopen(url)
    except HTTPError as e:    # 把错误保存到变量e中
        print('错误：', e)

