import socket

host = ''  # 相当于0.0.0.0
port = 12345
addr = (host,port)
s = socket.socket()  # 默认创建TCP套接字
# 默认程序后，系统为程序保留套接字1分钟，在1分钟内程序不能运行
# 通过下面选项的配置，使得程序在结束后可以立即再启动
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)  # 起动监听过程，最多允许1个客户机排队等待响应
cli_sock, cli_addr = s.accept()
print('客户机: ', cli_addr)
data = cli_sock.recv(1024)  # 最多一次接收1024字节数据
print(data.decode())   # 将bytes类型转成str类型
# 网络的数据要求是bytes类型，一般以\r\n结尾
cli_sock.send('Welcome\r\n'.encode())  # 将str转成bytes后发送
cli_sock.close()
s.close()

