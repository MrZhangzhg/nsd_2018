import urllib.error
from urllib import request

url1 = 'http://127.0.0.1/abc/'
url2 = 'http://127.0.0.1/ban/'

try:
    html = request.urlopen(url1)
except urllib.error.HTTPError as e:
    print('错误:', e)

print('*' * 40)

try:
    html = request.urlopen(url2)
except urllib.error.HTTPError as e:
    print('错误:', e)
