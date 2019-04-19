import socket

host = ''   # 表示0.0.0.0
port = 12345
addr = (host, port)
s = socket.socket()  # 默认创建TCP套接字
s.bind(addr)  # 绑定地址到套接字
s.listen(1)  # 启动监听过程  netstat -tlnp | grep :12345
cli_sock, cli_addr = s.accept()  # 等待客户端连接，收到连接返回(客户机套接字，客户机地址)
print('客户机: ', cli_addr)
data = cli_sock.recv(1024)  # 最多一次接收1024字节数据
print(data)
cli_sock.send(b'How are you?\r\n')  # 发送的数据必须是bytes类型
cli_sock.close()
s.close()

# yum install -y telnet; telnet 127.0.0.1 12345

