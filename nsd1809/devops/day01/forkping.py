import os
import subprocess

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )  # rc的值是ping命令的退出码
    if rc == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ['172.40.63.%s' % i for i in range(1, 255)]
    for ip in ips:
        ret_val = os.fork()
        if not ret_val:
            ping(ip)
            exit()
