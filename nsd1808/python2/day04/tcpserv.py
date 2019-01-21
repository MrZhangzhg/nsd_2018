import socket

host = ''    # 空串表示本机所有的地址，0.0.0.0
port = 1234
addr = (host, port)
s = socket.socket()   # 默认创建TCP套接字
# 设置选项，套接字随时可用
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 把地址绑定在套接字上
s.listen(1)   # 启动监听，1表示允许1个客户端
cli_sock, cli_addr = s.accept()  # 等待客户端连接，连接后返回客户机的套接字和地址
data = cli_sock.recv(1024)  # 最多接收1024字节数据
print(data)
cli_sock.send(b'Hello\r\n')  # 向客户端发送数据
cli_sock.close()
s.close()

# yum install -y telnet
# telnet x.x.x.x 1234
