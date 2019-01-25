import paramiko
import sys
import os
import getpass
import threading

def rcmd(host, user='root', passwd=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERROR:\n%s' % (host, err.decode()))
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
            t = threading.Thread(target=rcmd, args=(ip, 'root', password, command))
            t.start()
            # rcmd(ip, passwd=password, cmd=command)
