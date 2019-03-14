"""
1、发呆。脑补程序运行的样子：是交互的？非交互的？
交互的：屏幕提示？回答什么？
2、分析程序有哪些功能，将每个功能编写成函数。再从主程序部分定义函数什么时候调用
3、编写具体的函数
"""
import os

def get_fname():
    while True:
        fname = input('filename: ')
        if not os.path.exists(fname):   # 相当于[ ! -e fname ]
            break
        print('文件已存在，请重试。')

    return fname

def get_content():
    print('get content')

def wfile(fname, content):
    print('wfile')

if __name__ == '__main__':
    fname = get_fname()     # 获取文件名
    content = get_content()   # 获取文件内容
    wfile(fname, content)    # 将内容写到文件
