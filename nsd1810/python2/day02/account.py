import os
import pickle
import time

def save(fname):
    print('save')

def cost(fname):
    print('cost')

def query(fname):
    print('query')

def show_menu():
    fname = 'account.data'
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) 收入
(1) 开销
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    if not os.path.exists(fname):
        line = [time.strftime('%Y-%m-%d'), 0, 0, 10000, 'init']
        with open(fname, 'wb') as fobj:
            pickle.dump([line], fobj)

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效输入，请重试')
            continue
        if choice == '3':
            print('\nBye-bye')
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
