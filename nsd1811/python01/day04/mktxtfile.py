import os

def get_fname():
    while True:
        fname = input('文件名: ')
        if not os.path.exists(fname):
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    content = []
    print('请输入数据，在单独一行输入end结束。')
    while True:
        line = input('> ')
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
    content = [line + '\n' for line in content]  # 将列表每一项加上\n，否则没有换行
    wfile(fname, content)
