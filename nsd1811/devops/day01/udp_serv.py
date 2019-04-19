import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)  # UDP的type是SOCK_DGRAM
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

data, cli_addr = s.recvfrom(1024)  # 一次最多接收1024字节数据，返回值是(数据，客户机地址)
print(data.decode(), end='')
s.sendto(b'Hello World\r\n', cli_addr)  # 向客户机地址发送数据

s.close()


