import getpass

userdb = {}

def register():
    username = input('username: ').strip()
    if username in userdb:
        print('用户已存在')
    else:
        password = input('password: ')
        userdb[username] = password

def login():
    username = input('username: ').strip()
    password = getpass.getpass('password: ')
    # if username in userdb and userdb[username] == password:
    if userdb.get(username) == password:
        print('登陆成功')
    else:
        print('登陆失败')


def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) register
(1) login
(2) quit
Please input your choice(0/1/2): """

    while True:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('Invalid choice. Try again.')
            continue

        if choice == '2':
            print('Bye-bye')
            break

        cmds[choice]()

if __name__ == '__main__':
    show_menu()
