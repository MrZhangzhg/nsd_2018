from urllib.request import urlopen
from urllib.error import HTTPError

url1 = 'http://127.0.0.1/abc'
url2 = 'http://127.0.0.1/ban'

try:
    html1 = urlopen(url1)
except HTTPError as e:
    print('错误：', e)

try:
    html2 = urlopen(url2)
except HTTPError as e:
    print('错误：', e)
