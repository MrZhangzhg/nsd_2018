import sys
import randpass2    # 自己写的模块文件
import subprocess

def adduser(username, password, userfile):
    user_info = """username: %s
password: %s
""" % (username, password)   # 写入文件的用户信息
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (password, username),
        shell=True
    )
    with open(userfile, 'a') as fobj:
        fobj.write(user_info)   # 把用户信息写入文件

if __name__ == '__main__':
    password = randpass2.gen_pass()
    adduser(sys.argv[1], password, '/tmp/user.info')
