#SocketServer Tcp Client

from socket import *


HOST='LocalHost'
PORT=21567
BUFSIZ=1024
ADDR=(HOST,PORT)


While True:
    tcpCliSock=Socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data=input('>')
    if not data:
        break
    tcpCliSock.send('%s\r\n' %data)
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.strip)
    tcpCliSock.close()
