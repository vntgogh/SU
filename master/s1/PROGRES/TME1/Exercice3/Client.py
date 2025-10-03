from socket import *

serverName = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = "abc"
clientSocket.send(message)
modifiedMessage = clientSocket.recv(2048).decode('utf-8')

print(modifiedMessage)

clientSocket.close()