from socket import *
import time
from struct import *


serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')
while True:
    connectionSocket, address = serverSocket.accept()
    temps_client = connectionSocket.recv(2048)

    print("temps client : ",unpack('!d',temps_client)[0], " secondes")

    temps_serv = time.time()
    print("temps serveur : ", temps_serv, " secondes")

    connectionSocket.send(pack('!d',temps_serv))
    connectionSocket.close()
