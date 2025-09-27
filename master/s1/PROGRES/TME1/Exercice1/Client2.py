from socket import *
import time

ipServeur = gethostname() 
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_DGRAM)
message = "def".encode('utf-8')
debut = time.time()
clientSocket.sendto(message,(ipServeur ,serverPort))    
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode('utf-8'))
clientSocket.close()
fin = time.time()
print("RTT : ", fin-debut, "s")