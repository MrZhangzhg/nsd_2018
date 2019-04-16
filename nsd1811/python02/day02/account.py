import os
import pickle
from time import strftime

def save(fname):


def cost(fname):


def query(fname):


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    fname = 'record.data'
    if not os.path.exists(fname):
        date = strftime('%Y-%m-%d')
        data = [
            [date, 0, 0, 10000, 'init data']
        ]
        with open(fname, 'wb') as fobj:
            pickle.dump(data, fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            break

        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
