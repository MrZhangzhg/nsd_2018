import getpass

userdb = {}

def register():
    username = input('username: ')
    if username not in userdb:
        password = input('password: ')
        userdb[username] = password
    else:
        print('用户已存在')

def login():
    username = input('username: ')
    password = getpass.getpass("password: ")
    # if username not in userdb or userdb[username] != password:
    if userdb.get(username) != password:
        print('登陆失败')
    else:
        print('登陆成功')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('无效输入，请重试')
            continue
        if choice == '2':
            print('Bye-bye')
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
