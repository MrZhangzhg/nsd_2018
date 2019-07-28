import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)  # 创建UDP套接字
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

# 一次最多接收1024字节数据，返回元组(数据，客户机地址信息)
data, cli_addr = s.recvfrom(1024)
print(data.decode())
s.sendto('欢迎\r\n'.encode(), cli_addr)
s.close()

