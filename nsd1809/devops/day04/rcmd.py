import paramiko

def rcmd(host, user='root', password=None, port=22, command=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, port=port)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:  # 如果有输出或错误则打印在屏幕上
        print('[\033[32;1mOUT\033[0m] %s:\n%s' % (host, out.decode()))
    if err:
        print('[\033[31;1mERROR\033[0m] %s:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    rcmd('192.168.4.4', password='123456', command='id root; id tom')
