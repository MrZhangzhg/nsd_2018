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
        print()
        break
    print('客户机: ', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        print(data.decode(), end='')
        sdata = input('> ') + '\r\n'  # input读入的是str类型
        cli_sock.send(sdata.encode())  # 转成bytes类型发送
    cli_sock.close()

s.close()
