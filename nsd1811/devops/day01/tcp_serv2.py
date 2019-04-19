import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
cli_sock, cli_addr = s.accept()
print('客户机: ', cli_addr)
while True:
    data = cli_sock.recv(1024)
    if data.strip() == b'quit':
        break
    print(data.decode(), end='')
    cli_sock.send(b'How are you?\r\n')
cli_sock.close()
s.close()


