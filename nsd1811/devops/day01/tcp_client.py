import socket

server = '192.168.4.254'
port = 12345
addr = (server, port)  # 要连接的服务器地址
c = socket.socket()
c.connect(addr)   # 连接服务器

while True:
    data = input('(quit to end)> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break
    rdata = c.recv(1024)   # 一次最多接收1024字节数据
    print(rdata.decode(), end='')

c.close()



