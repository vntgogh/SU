from socket import *

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')

while True:
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(2048).decode('utf-8')

    print("Message de ", address, " : ", message.encode('utf-8'))

    modifiedMessage = message.upper().encode('utf-8')
    connectionSocket.send(modifiedMessage)
    connectionSocket.close()