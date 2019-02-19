def save():


def cost():


def query():


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
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
        cmds[choice]()


if __name__ == '__main__':
    show_menu()
