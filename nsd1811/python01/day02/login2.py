import getpass   # 导入名为getpass的模块

username = input('username: ')
password = getpass.getpass('password: ')  # 调用getpass模块中的getpass功能

if username == 'bob' and password == '123456':
    print('登陆成功')
else:
    print('登陆失败')
