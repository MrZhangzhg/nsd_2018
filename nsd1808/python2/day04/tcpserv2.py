import socket

host = ''
port = 1234
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

    while True:
        data = cli_sock.recv(1024)    # 接收的数据是bytes类型
        if data.strip() == b'quit':
            break
        print(data.decode(), end='')   # 把bytes转为str输出
        send_data = input('> ') + '\r\n'
        cli_sock.send(send_data.encode())   # 把str转发bytes发送

    cli_sock.close()

s.close()
