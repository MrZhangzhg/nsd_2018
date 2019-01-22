import socket
import os
from time import strftime

class TcpTimeServer:
    def __init__(self, host='', port=1234):
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
            data = "[%s] %s" % (strftime('%H:%M:%S'), data.decode())
            cli_sock.send(data.encode())

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()   # 接受客户端
            except KeyboardInterrupt:
                break
            ret_val = os.fork()
            if not ret_val:
                self.serv.close()      # 子进程关闭服务器套接字
                self.chat(cli_sock)    # 与客户端通信
                cli_sock.close()       # 关闭客端连接
                exit()
            cli_sock.close()     # 父进程关闭客户端套接字

            while True:
                result = os.waitpid(-1, 1)  # 先处理僵尸进程
                print(result)
                if result[0] == 0:
                    break

        self.serv.close()

if __name__ == '__main__':
    tcp_serv = TcpTimeServer()
    tcp_serv.mainloop()
