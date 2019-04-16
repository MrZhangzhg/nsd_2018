import os
import pickle
from time import strftime

def save(fname):
    amount = int(input('金额: '))
    comment = input('说明: ')
    date = strftime('%Y-%m-%d')   # 获取当前日期
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)      # 从文件中取出全部记录
        balance = data[-1][-2] + amount   # 文件最后一行的倒数第2项是余额

    line = [date, amount, 0, balance, comment]
    data.append(line)  # 把最新记录加入到大列表

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)  # 把大列表写到文件

def cost(fname):
    amount = int(input('金额: '))
    comment = input('说明: ')
    date = strftime('%Y-%m-%d')  # 获取当前日期
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)  # 从文件中取出全部记录
        balance = data[-1][-2] - amount  # 文件最后一行的倒数第2项是余额

    line = [date, 0, amount, balance, comment]
    data.append(line)  # 把最新记录加入到大列表

    with open(fname, 'wb') as fobj:
        pickle.dump(data, fobj)  # 把大列表写到文件

def query(fname):
    with open(fname, 'rb') as fobj:
        data = pickle.load(fobj)

    # 打印表头
    print('%-15s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    for line in data:
        print('%-15s%-8s%-8s%-12s%-20s' % tuple(line))  # 将列表转成元组

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
