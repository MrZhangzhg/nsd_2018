stack = []   # 全局变量定义后，在后面任何位置都可见可用

def push_it():
    item = input('内容: ').strip()
    if item:  # 如果字符串非空
        stack.append(item)

def pop_it():
    if stack:  # 如果列表非空
        print('从栈中弹出: %s' % stack.pop())
    else:
        print('空栈')

def view_it():
    print('\033[31;1m%s\033[0m' % stack)

def show_menu():
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    # 注意：字典中的函数不要加()，因为是把函数存入字典，而不是把函数的执行结果存入
    prompt = """(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): """

    while True:
        choice = input(prompt).strip()[0]  # 删除用户输入的两端空格，并取出第一个字符
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入，请重试。')
            continue

        if choice == '3':
            print('Bye-bye')
            break

        cmds[choice]()  # 在字典中取出函数，加上()，进行调用

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
