import socket

host = ''
port = 12345
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    sdata = input('> ') + '\r\n'
    if sdata.strip() == 'quit':
        break
    c.sendto(sdata.encode(), addr)
    data, ser_addr = c.recvfrom(1024)
    print(data.decode())
c.close()
