from urllib import request

html = request.urlopen('https://upload-images.jianshu.io/upload_images/14715425-a69dcd608265e3e4.png')
with open('/tmp/aaa.png', 'wb') as fobj:
    while True:
        data = html.read(1024)
        if not data:
            break
        fobj.write(data)


