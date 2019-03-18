import os
import pickle
import time

def save(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:   # 取出所有记录的列表
        records = pickle.load(fobj)
    balance = records[-1][-2] + amount  # 计算最新余额
    records.append([date, amount, 0, balance, comment])  # 追加新记录
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

def cost(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:  # 取出所有记录的列表
        records = pickle.load(fobj)
    balance = records[-1][-2] - amount  # 计算最新余额
    records.append([date, 0, amount, balance, comment])  # 追加新记录
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)

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
