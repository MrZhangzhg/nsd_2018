import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)  # 待连接的服务器地址
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)
    # info = c.recvfrom(1024)   # (数据，服务器地址)
    data = c.recvfrom(1024)[0]
    print(data.decode(), end='')

c.close()
