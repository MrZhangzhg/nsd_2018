def register():
    print('register')

def login():
    print('login')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请做出选择(0/1/2): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效选择，请重试！')
            continue
        if choice == '2':
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
