import os

def get_fname():
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []
    while True:
        line = input('("end" to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = [line + '\n' for line in content]  # 为每行加上回车
    wfile(fname, content)
