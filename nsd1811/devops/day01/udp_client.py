import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)  # 待连接的服务器地址
c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'ni hao\r\n', addr)
info = c.recvfrom(1024)
print(info)
