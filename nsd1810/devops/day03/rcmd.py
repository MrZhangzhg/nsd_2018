import paramiko
import sys
import getpass

def rcmd(host=None, port=22, user='root', passwd=None, command=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=passwd, port=port)
    _, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERROR:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.4.6', passwd='123456', command='id root; id wangwu')
    ipfile = sys.argv[1]
    command = sys.argv[2]
    password = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 删除行尾的\n
            rcmd(ip, passwd=password, command=command)
