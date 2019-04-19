import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)  # UDP的type是SOCK_DGRAM
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)


while True:
    try:
        data, cli_addr = s.recvfrom(1024)  # 一次最多接收1024字节数据，返回值是(数据，客户机地址)
    except KeyboardInterrupt:
        print()
        break
    data = data.decode()  # bytes转str
    print(data, end='')
    rdata = '[%s] %s' % (strftime('%H:%M:%S'), data)
    s.sendto(rdata.encode(), cli_addr)  # 向客户机地址发送数据

s.close()
