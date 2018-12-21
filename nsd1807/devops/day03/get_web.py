import sys
from urllib.request import urlopen

def download(url, fname):
    html = urlopen(url)
    with open(fname, 'wb') as fobj:
        while True:
            data = html.read(1024)
            if not data:
                break
            fobj.write(data)

if __name__ == '__main__':
    download(sys.argv[1], sys.argv[2])
