import socket

server = '192.168.4.254'
port = 1234
addr = (server, port)   # 要连接的服务器地址
c = socket.socket()
c.connect(addr)

while True:
    data = input('> ') + '\r\n'
    c.send(data.encode())   # 把str转发bytes发送
    if data.strip() == 'quit':
        break
    recv_data = c.recv(1024)
    print(recv_data.decode(), end='')

c.close()
