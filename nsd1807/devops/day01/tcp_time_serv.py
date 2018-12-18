import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    cli_sock, cli_addr = s.accept()
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
        cli_sock.send(data.encode())

    cli_sock.close()

s.close()








