from urllib import request, error

url1 = 'http://127.0.0.1/abcd'
url2 = 'http://127.0.0.1/ban'
try:
    r1 = request.urlopen(url1)
except error.HTTPError as e:  # 把异常捕获后起名为e，e只是个变量
    print('错误:', e)

try:
    r2 = request.urlopen(url2)
except error.HTTPError as e:
    print('错误:', e)
