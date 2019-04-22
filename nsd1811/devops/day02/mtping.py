import threading
import subprocess

def ping(host):
    rc = subprocess.run(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if rc.returncode == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    iplist = ['172.40.63.%s' % i for i in range(1, 255)]
    for ip in iplist:
        t = threading.Thread(target=ping, args=(ip,))
        t.start()
