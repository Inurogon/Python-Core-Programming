#TCP_Socket Server
from socket import *
from time import ctime

HOST=' '
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)


while True:
    print('Waiting for Connection...')
    data,ADDR=tcpSerSock.accept()
    print('Connected From',ADDR)
    while True:
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
           break
        tcpCliSock.send('[%s] %s' % (bytes(ctime(),'utf-8'),data))
    tcpCliSock.close()
tcpSerSock.close()
        
