import socket
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
            self.chat(cli_sock)

        self.serv.close()

if __name__ == '__main__':
    tcpserv = TcpTimeServer()
    tcpserv.run()
