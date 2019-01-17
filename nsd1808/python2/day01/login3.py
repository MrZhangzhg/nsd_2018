import getpass

userdb = {}

def register():
    username = input('username: ')
    if username in userdb:
        print('%s already exists' % username)
    else:
        password = input('password: ')
        userdb[username] = password

def login():
    username = input('username: ')
    password = getpass.getpass('password: ')
    # if username in userdb and userdb[username] == password:
    if userdb.get(username) == password:
        print('Login successful')
    else:
        print('Login incorrect')

def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) register
(1) login
(2) quit
Please input your choice(0/1/2): """
    while True:
        choice = input(prompt).strip()[0]
        if choice not in '012':
            print('Invalid input. Try again.')
            continue
        if choice == '2':
            break
        cmds[choice]()

if __name__ == '__main__':
    show_menu()
