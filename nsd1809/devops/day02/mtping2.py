import subprocess
import threading

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):  # 创建可调用的方法
        rc = subprocess.call(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if rc == 0:
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)

if __name__ == '__main__':
    ips = ['172.40.63.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(ip), args=())
        t.start()  # target()  => 调用实例，将执行__call__方法
