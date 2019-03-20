import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)  # udp必须指定type
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    data, cli_addr = s.recvfrom(1024)  # 返回发来的数据和客户机的地址
    print(cli_addr, data.decode())  # 将网络发来的bytes类型转换成str类型
    sdata = input('> ') + '\r\n'
    s.sendto(sdata.encode(), cli_addr)

s.close()
