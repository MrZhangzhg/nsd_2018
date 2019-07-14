stack = []

def push_it():
    data = input('item to push: ').strip()
    if data:  # 如果是非空字符串
        stack.append(data)

def pop_it():
    if stack:
        print('From stack popped:', stack.pop())
    else:
        print('Empty stack')

def view_it():
    print(stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) push
(1) pop
(2) view
(3) quit
Please input your choice(0/1/2/3): """

    while True:
        # 将函数存到字典中
        choice = input(prompt).strip()  # 去除用户输出的额外的空格
        if choice not in ['0', '1', '2', '3']:
            print('Invalid choice. Try again.')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()

        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # elif choice == '2':
        #     view_it()
        # else:
        #     print('Bye-bye')
        #     break

if __name__ == '__main__':
    show_menu()
