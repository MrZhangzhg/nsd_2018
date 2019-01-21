import socket

server = '192.168.4.254'
port = 1234
addr = (server, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)
    recv_info = c.recvfrom(1024)
    # print(recv_info)
    recv_data = recv_info[0]
    print(recv_data.decode(), end='')

c.close()
