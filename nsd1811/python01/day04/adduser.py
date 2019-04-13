import sys
import subprocess
from randpass2 import gen_pass

def adduser(user, passwd, fname):
    info = '''用户信息：
用户名: %s
密码: %s
''' % (user, passwd)

    subprocess.run('useradd %s' % user, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user),
        shell=True
    )

    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    pwd = gen_pass()
    filename = '/tmp/users.txt'
    adduser(username, pwd, filename)
