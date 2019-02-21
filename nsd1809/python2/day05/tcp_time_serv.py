import socket
from time import strftime

class TcpTimeServ:
    def __init__(self, host, port):
        '初始化结束后，生成一个可以用的TCP套接字'
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            data = data.decode()
            if data.strip() == 'quit':
                break
            sdata = "[%s] %s" % (strftime('%H:%M:%S'), data)
            cli_sock.send(sdata.encode())

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            self.chat(cli_sock)
            cli_sock.close()

        self.serv.close()

if __name__ == '__main__':
    tcp = TcpTimeServ(host='', port=12345)  # 调用__init__
    tcp.mainloop()
