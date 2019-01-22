import socket
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
            self.chat(cli_sock)    # 与客户端通信
            cli_sock.close()       # 关闭客端连接

        self.serv.close()

if __name__ == '__main__':
    tcp_serv = TcpTimeServer()
    tcp_serv.mainloop()
