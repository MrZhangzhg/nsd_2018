import socket

host = '127.0.0.1'
port = 12345
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)
    rdata, serv_addr = c.recvfrom(1024)
    print(rdata.decode())

c.close()
