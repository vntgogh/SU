from socket import *
import time
import random

ipServeur = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
sum = 0.0
message = "def"

for i in range(5):
    debut = time.time()
    clientSocket.sendto(message.encode('utf-8'), (ipServeur, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    fin = time.time()
    sum += fin-debut
    print(modifiedMessage.decode('utf-8'))
    print("RTT : ",fin-debut,"s")
print("Moyenne des RTT : ", sum, "s")
clientSocket.close()


