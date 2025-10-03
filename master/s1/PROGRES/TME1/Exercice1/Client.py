from socket import *
import time
import random

ipServeur = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
sum = 0.0
message = "abc"

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

# Probabilité de 0.5
# for i in range(5):
#     delay = 0.1
#     if random.random() < 0.5:
#         while True:
#             clientSocket.settimeout(delay)
#             try:
#                 debut = time.time()
#                 clientSocket.sendto(message.encode('utf-8'), (ipServeur, serverPort))
#                 modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#                 fin = time.time()
#                 sum += fin-debut
#                 print(modifiedMessage.decode('utf-8'))
#                 print(f"RTT : ",fin-debut,"s")
#             except timeout:
#                 delay *= 2
#                 if delay > 2.0:
#                     raise RuntimeError('server seems down')
#             else:
#                 break
# print("Moyenne des RTT : ", sum, "s")
# clientSocket.close()

