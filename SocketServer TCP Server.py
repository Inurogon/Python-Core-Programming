#SocketServer Tcp Server

from SocketServer import (TcpServer as TCP,SteamRequestHandler as SRH)
from time import ctime



HOST=' '
PORT=21567
ADDR=(HOST,PORT)


class MyRequestHandler(SRH):
    def handle(self)
        print('...connected from:',self.client_address)
        self.wfile.write('[%s] %s' % (ctime()),self.refile.readline())

tcpServ=Tcp(ADDR,MyRequestHandler)
print('Waiting for connection')
tcpServ.serve_forever()




