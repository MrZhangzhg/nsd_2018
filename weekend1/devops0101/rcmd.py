import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, user, passwd, command, port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.4.5', 'root', '123456', 'id root; id john')
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print('No shuch file:', sys.argv[1])
        exit(2)

    ipfile = sys.argv[1]
    command = sys.argv[2]
    passwd = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()  # 去掉行尾的\n
            # rcmd(ip, 'root', passwd, command)
            t = threading.Thread(target=rcmd, args=(ip, 'root', passwd, command))
            t.start()
