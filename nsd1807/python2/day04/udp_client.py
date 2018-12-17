import socket

host = ''
port = 12345
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'Nice to meet you!\r\n', addr)
data, ser_addr = c.recvfrom(1024)
print(data.decode())
c.close()
