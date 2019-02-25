from urllib import request

# html = request.urlopen('http://www.baidu.com')
# data = html.read()  # 读出来的是网络数据，默认是bytes类型
# with open('/tmp/bd.html', 'wb') as fobj:
#     fobj.write(data)

def download(url, fname):
    html = request.urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download('https://upload-images.jianshu.io/upload_images/12347101-9527fb424c6e973d.png', '/tmp/image1.jpeg')
