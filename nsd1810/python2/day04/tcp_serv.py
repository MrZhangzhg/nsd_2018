import socket

host = ''    # 监听在0.0.0.0
port = 12345
addr = (host, port)
s = socket.socket()  # 默认创建TCP协议的套接字
# 默认情况下，程序结束后，系统会保留这个套接字1分钟，1分钟内不能使用相同的
# 端口号再次启动，加上以下一行选项设置，允许服务仍然使用这个端口
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)  # 允许多少个客户端排队等候，数字是多少都没用
# accept接受客户机的连接，返回客户机的套接字和地址
cli_sock, cli_addr = s.accept()
data = '吃了吗？\r\n'  # 网络数据一般都以\r\n结尾
cli_sock.send(data.encode())   # 将str类型转成bytes类型发送
rdata = cli_sock.recv(1024)  # 最多一次接收1024字节
print(rdata.decode())  # 把网络上接收的bytes类型转成str类型
cli_sock.close()
s.close()
# yum install -y telnet; telnet 127.0.0.1 12345
