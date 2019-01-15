import os

def get_fname():
    while True:
        fname = input('文件名: ')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试')

    return fname

def get_content():
    content = []

    print('请输入内容，输入end表示结束')
    while True:
        line = input('> ')
        if line == 'end':
            break
        content.append(line)   # 用户输入的内容追加到列表

    return content

def wfile(fname, content):
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    content = ["%s\n" % line for line in content]
    wfile(fname, content)
