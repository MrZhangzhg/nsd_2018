import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, user='root', passwd=None, port=22, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    error = stderr.read()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out.decode()))
    if error:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, error.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: %s ipfile 'command'" % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('No such file:', ipfile)
        exit(2)
    passwd = getpass.getpass()
    command = sys.argv[2]
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            # rcmd(ip, passwd=passwd, cmd=command)
            t = threading.Thread(target=rcmd, args=(ip,), kwargs={'passwd': passwd, 'cmd': command})
            t.start()
            # target(*args, **kwargs)
            # target(ip, passwd=passwd, cmd=command)
