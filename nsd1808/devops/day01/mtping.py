import threading
import subprocess

def ping(host):
    rc = subprocess.call('ping -c2 %s &> /dev/null' % host, shell=True)
    if rc == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('172.40.84.%s' % i for i in range(1, 255))
    for ip in ips:    # 主线程用于产生工作线程
        # ping(ip)
        t = threading.Thread(target=ping, args=(ip,))
        t.start()   # 调用target(ip)，工作线程做具体工作
