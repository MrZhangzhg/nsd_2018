import sys
import subprocess
import randpass2

def adduser(username, password, fname):
    info = """用户信息：
用户名：%s
密码：%s
""" % (username, password)
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    password = randpass2.randpass()
    fname = '/tmp/mima.txt'
    adduser(sys.argv[1], password, fname)
