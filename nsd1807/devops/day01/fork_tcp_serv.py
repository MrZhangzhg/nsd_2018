import socket
import os
from time import strftime

class TcpServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind(self.addr)
        self.s.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())

    def run(self):
        while True:
            cli_sock, cli_addr = self.s.accept()
            retval = os.fork()
            if not retval:
                self.s.close()  # 子进程只与客户机通信，用不到服务器套接字
                self.chat(cli_sock)
                cli_sock.close()
                exit()
            cli_sock.close()    # 父进程只负责接收新客户端，用不到客户机套接字

            while True:
                result = os.waitpid(-1, 1)  # 优先处理僵尸进程
                print(result)
                if result[0] == 0:   # 如果没有僵尸进程，跳出循环
                    break

        s.close()

if __name__ == '__main__':
    server = TcpServer()
    server.run()
