import paramiko

def rcmd(host=None, port=22, user='root', passwd=None, command=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=passwd)
    _, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERROR:\n%s' % (host, err.decode()))
    ssh.close()


if __name__ == '__main__':
    rcmd('192.168.4.6', passwd='123456', command='id root; id wangwu')
