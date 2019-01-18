import os
import time
import pickle

def save(fname):
    amount = int(input('amount: '))   # 金额：
    comment = input('comment: ')      # 备注
    date = time.strftime('%Y-%m-%d')   # 当前日期
    with open(fname, 'rb') as fobj:
        all_records = pickle.load(fobj)   # 从文件中load出来看数据是列表
    # 列表的最后一项是最新存入的数据，它是一个元组，元组倒数第二项是余额
    balance = all_records[-1][-2] + amount
    record = (date, 0, amount, balance, comment)
    all_records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(all_records, fobj)

def cost(fname):
    amount = int(input('amount: '))
    comment = input('comment: ')
    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        all_records = pickle.load(fobj)
    balance = all_records[-1][-2] - amount
    record = (date, amount, 0, balance, comment)
    all_records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(all_records, fobj)

def query(fname):
    with open(fname, 'rb') as fobj:
        all_records = pickle.load(fobj)
    # 先打印出表头
    print('%-12s%-8s%-8s%-10s%-20s' % ('date', 'cost', 'save', 'balance', 'comment'))
    # 在表头下面，打印出每一行记录
    for record in all_records:
        print('%-12s%-8s%-8s%-10s%-20s' % record)

def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = """(0) save
(1) cost
(2) query
(3) quit
Please input your choice(0/1/2/3): """
    fname = 'account.data'
    if not os.path.exists(fname):
        init_data = [(time.strftime('%Y-%m-%d'), 0, 0, 10000, 'init')]
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('Invalid input. Try again.')
            continue
        if choice == '3':
            break
        cmds[choice](fname)

if __name__ == '__main__':
    show_menu()
