import os
import pickle
from time import strftime


def init_data(fname):
    data = [
        [strftime('%Y-%m-%d'), 0, 0, 10000, 'init']
    ]
    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)

def save(fname):
    print('save')

def cost(fname):
    print('cost')

def query(fname):
    print('query')


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    fname = 'record.data'
    if not os.path.exists(fname):   # 如果文件不存在，则初始化
        init_data(fname)
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请做出你的选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()
        if choice not in [str(i) for i in range(4)]:
            print('无效的输入，请重试！')
            continue
        if choice == '3':
            print('\nBye-bye')
            break
        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
