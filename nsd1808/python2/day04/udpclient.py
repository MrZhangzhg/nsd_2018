import socket

server = '192.168.4.254'
port = 1234
addr = (server, port)
c = socket.socket(type=socket.SOCK_DGRAM)

c.sendto(b'hello world!\r\n', addr)
recv_info = c.recvfrom(1024)
print(recv_info)
recv_data = recv_info[0]
print(recv_data.decode(), end='')
c.close()
