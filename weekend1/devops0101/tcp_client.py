import socket

server = '127.0.0.1'
port = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)
c.send('你好\r\n'.encode())
data = c.recv(1024)
print(data.decode())
c.close()

