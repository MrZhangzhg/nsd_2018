import socket

host = ''     # 代表0.0.0.0
port = 12345  # 应该大于1024
addr = (host, port)
s = socket.socket()  # 默认使用TCP协议
# 设置套接字选项，使得服务程序结束后可立即再启动
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)  # 一般只能写到5以内，表示允许多少客户端排队访问
cli_sock, cli_addr = s.accept()
print('客户端：', cli_addr)
data = cli_sock.recv(1024)  # 相当于fobj.read(1024)
print(data)
print(data.decode())
sdata = '欢迎!\r\n'
cli_sock.send(sdata.encode())   # 放送的数据必需是bytes类型，二进制
cli_sock.close()
s.close()
# yum install -y telnet
