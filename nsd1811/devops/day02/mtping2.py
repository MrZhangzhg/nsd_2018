import threading
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        rc = subprocess.run(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if rc.returncode == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)

if __name__ == '__main__':
    iplist = ['172.40.63.%s' % i for i in range(1, 255)]
    for ip in iplist:
        t = threading.Thread(target=Ping(ip))  # target是Ping的实例
        t.start()  # target()
