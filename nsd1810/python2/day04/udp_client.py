import socket

server = '127.0.0.1'
port = 12345
addr = (server, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('(quit to stop)> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)  # 发送数据到addr(服务器地址)
    rdata, serv_addr = c.recvfrom(1024)   # 收到是服务器发来的数据和服务器地址
    print(serv_addr, rdata.decode())  # 需要把rdata从bytes类型转为str类型

c.close()
