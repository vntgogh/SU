from socket import *
from datetime import datetime

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print('server ready')
while True:
    connectionSocket, address = serverSocket.accept()
    message = connectionSocket.recv(2048).decode('utf-8')

    print(message)

    server_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') [:-3]

    modifiedMessage = server_time.encode('utf-8')

    connectionSocket.send(modifiedMessage)
    connectionSocket.close()

"""
Prompt : Quelle fonction en Python permet de donner l'heure en temps réel avec les secondes ?'
"""