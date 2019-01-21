import socket
from time import strftime

host = ''
port = 1234
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    try:
        data, cli_addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    print(data.decode(), end='')
    data = "[%s] %s" % (strftime('%H:%M:%S'), data.decode())
    s.sendto(data.encode(), cli_addr)

s.close()
