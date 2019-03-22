import socket
import os
from time import strftime

class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = data.decode()  # 将bytes转为str
            data = '[%s] %s' % (strftime('%H:%M:%S'), data)
            cli_sock.send(data.encode())

        cli_sock.close()

    def run(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            retval = os.fork()
            # fork后，父子进程中都有服务器套接字和客户端套接字
            if not retval:
                self.serv.close()  # 子进程不需要服务器套接字，所以关掉
                self.chat(cli_sock)
                exit()

            cli_sock.close()  # 父进程不与客户机通信，所以把客户机套接字关闭

        self.serv.close()

if __name__ == '__main__':
    tcpserv = TcpTimeServer()
    tcpserv.run()
