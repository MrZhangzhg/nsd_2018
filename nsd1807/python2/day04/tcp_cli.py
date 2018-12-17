import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)   # 客户机要连接的服务器的信息

c = socket.socket()
c.connect(addr)
c.send(b'Hello World!\r\n')
data = c.recv(1024)
print(data.decode(), end='')
c.close()
