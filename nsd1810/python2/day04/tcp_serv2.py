import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    print('客户端：', cli_addr)

    while True:
        rdata = cli_sock.recv(1024)
        if rdata.strip() == b'quit':
            cli_sock.send(b'Bye-bye\r\n')
            break
        print(rdata.decode())
        data = input('> ') + '\r\n'
        cli_sock.send(data.encode())

    cli_sock.close()

s.close()
