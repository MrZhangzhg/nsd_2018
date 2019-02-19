import os
import pickle
from time import strftime

def init_data(fname):
    """数据的形式[时间, 收入, 开销, 余额, 备注]
    [
        ['2019-2-19', 0, 0, 10000, 'init'],
        ['2019-2-19', 15000, 0, 25000, 'salary'],
    ]
    """
    data = [
        [strftime('%Y-%m-%d'), 0, 0, 10000, 'init']
    ]
    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)

def save(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        record_list = pickle.load(fobj)     # 取出存储的列表
    balance = record_list[-1][-2] + amount  # 计算最新余额
    record_list.append([date, amount, 0, balance, comment])
    with open(fname, 'wb') as fobj:   # 把数据列表覆盖回文件
        pickle.dump(record_list, fobj)

def cost(fname):
    amount = int(input('金额: '))
    comment = input('备注: ')
    date = strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        record_list = pickle.load(fobj)  # 取出存储的列表
    balance = record_list[-1][-2] - amount
    record_list.append([date, 0, amount, balance, comment])
    with open(fname, 'wb') as fobj:  # 把数据列表覆盖回文件
        pickle.dump(record_list, fobj)

def query(fname):
    with open(fname, 'rb') as fobj:
        record_list = pickle.load(fobj)

    print('%-14s%-10s%-10s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for record in record_list:  # 从大列表中取出小列表
        # tuple用于将数据转成列表
        print('%-14s%-10s%-10s%-12s%-20s' % tuple(record))

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
