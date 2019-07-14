import os

def get_fname():
    '用于获取文件名'
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):  # 文件不存在则中断循环
            break
        print('File already exists. Try again.')

    return fname

def get_content():
    '用于获取内容'
    content = []

    print('请输入内容，输入end结束')
    while True:
        line = input('(end to quit)> ')
        if line == 'end':
            break
        content.append(line)

    return content

def wfile(fname, content):
    '用于将内容写入文件'
    with open(fname, 'w') as fobj:
        fobj.writelines(content)

if __name__ == '__main__':
    fname = get_fname()
    content = get_content()
    # content中的每个字符串项目，结尾没有\n，需要为其加上
    content = ['%s\n' % line for line in content]
    wfile(fname, content)
