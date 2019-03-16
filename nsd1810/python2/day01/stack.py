def push_it():


def pop_it():


def view_it():


def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}  # 把函数存入字典
    prompt = """(0) push it
(1) pop it
(2) view it
(3) quit
Please input your choice(0/1/2/3): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('Invalid input. Try again.')
            continue

        if choice == '3':
            break
        cmds[choice]()   # choice = '0' -> cmds['0']  ->push_it

        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     break


if __name__ == '__main__':
    show_menu()
