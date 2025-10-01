from socket import *

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('server ready')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)

    print(message, " de ", clientAddress)

    modifiedMessage = message.decode('utf-8').upper()

    serverSocket.sendto(modifiedMessage.encode('utf-8'),clientAddress)

"""
LLM utilisé : Perplexity
Prompt : 
- Que faut-il modifier chez le client pour tester notre serveur si le client et le serveur sont sur deux machiens différentes ?
"""