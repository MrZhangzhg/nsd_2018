import os
import pickle

def cost(record):


def save(record):


def query(record):


def show_menu():
    record = 'record.data'
    if not os.path.exists(record):
        init_data = [
            ['2018-12-13', 0, 0, 10000, '开始记账'],
        ]
        with open(record, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    cmds = {'0': cost, '1': save, '2': query}
    prompt = """(0) 记录开销
(1) 记录收入
(2) 查询收支
(3) 退出
请选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0/1/2/3':
            print('无效输入，请重试')
            continue
        if choice == '3':
            print('Bye-bye')
            break
        cmds[choice](record)

if __name__ == '__main__':
    show_menu()
