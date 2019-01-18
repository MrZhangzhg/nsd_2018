import os
import time
import pickle

def save(fname):
    print('save')

def cost(fname):
    pass

def query(fname):
    pass

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
