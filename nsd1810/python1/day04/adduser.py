import subprocess
import randpass2
import sys

def adduser(username, password, fname):
    info = """user info:
username:%s
password:%s
""" % (username, password)
    subprocess.run('useradd %s' % username, shell=True)
    subprocess.run(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )
    with open(fname, 'a') as fobj:
        fobj.write(info)

if __name__ == '__main__':
    username = sys.argv[1]
    password = randpass2.randpass()
    fname = '/tmp/user.txt'
    adduser(username, password, fname)
