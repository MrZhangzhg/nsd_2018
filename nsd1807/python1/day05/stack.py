stack = []   # 全局变量从定义开始一直到程序结束，任何地方都可见、可用

def push_it():
    item = input('数据: ').strip()
    if item:
        stack.append(item)

def pop_it():
    if stack:
        print('从栈中弹出了%s' % stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')

def view_it():
    print('\033[32;1m%s\033[0m' % stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '0123':
            print('无效输入，请重试')
            continue
        if choice == '3':
            print('Bye-bye')
            break
        cmds[choice]()
        # if choice == '0':
        #     push_it()
        # elif choice == '1':
        #     pop_it()
        # else:
        #     view_it()

if __name__ == '__main__':
    show_menu()
