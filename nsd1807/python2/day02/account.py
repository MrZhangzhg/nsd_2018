import os
import pickle
import time

def cost(record):
    amount = int(input('金额：'))
    comment = input('备注：')
    date = time.strftime('%Y-%m-%d')
    with open(record, 'rb') as fobj:
        data = pickle.load(fobj)
    balance = data[-1][-2] - amount
    data.append([date, 0, amount, balance, comment])
    with open(record, 'wb') as fobj:
        pickle.dump(data, fobj)

def save(record):
    amount = int(input('金额：'))
    comment = input('备注：')
    date = time.strftime('%Y-%m-%d')
    with open(record, 'rb') as fobj:
        data = pickle.load(fobj)
    balance = data[-1][-2] + amount
    data.append([date, amount, 0, balance, comment])
    with open(record, 'wb') as fobj:
        pickle.dump(data, fobj)

def query(record):
    print('%-12s%-10s%-10s%-10s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(record, 'rb') as fobj:
        data = pickle.load(fobj)
    for item in data:
        print('%-12s%-10s%-10s%-10s%-20s' % tuple(item))

def show_menu():
    record = 'record.data'
    if not os.path.exists(record):
        init_data = [
            [time.strftime('%Y-%m-%d'), 0, 0, 10000, '开始记账'],
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
        try:
            choice = input(prompt).strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in '0/1/2/3':
            print('无效输入，请重试')
            continue
        if choice == '3':
            print('\nBye-bye')
            break
        cmds[choice](record)

if __name__ == '__main__':
    show_menu()
