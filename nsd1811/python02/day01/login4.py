import getpass

userdb = {}

def register():
    user = input('用户名: ').strip()
    if user and user not in userdb:
        passwd = input('密码: ')
        userdb[user] = passwd
    else:
        print('用户名不能为空，或用户名已存在')

def login():
    user = input('用户名: ')
    passwd = getpass.getpass('密码: ')   # abc
    if userdb.get(user) == passwd: # 如果用户不在字典中返回值为None，否则返回它的密码
        print('登陆成功')
    else:
        print('登陆失败')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登陆
(2) 退出
请选择(0/1/2): """
    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('无效的选择，请重试。')
            continue

        if choice == '2':
            print('Bye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
