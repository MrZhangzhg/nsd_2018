import paramiko
import getpass
import sys
import os
import threading

def rcmd(host, password=None, command=None, port=22, user='root'):
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
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    command = sys.argv[2]
    password = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, password=password, command=command)
            t = threading.Thread(target=rcmd, args=(ip, password, command))
            t.start()  # target(ip, password, command)
