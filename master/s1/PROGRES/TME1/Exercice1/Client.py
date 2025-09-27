from socket import *
import time
import random

ipServeur = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
sum = 0.0

for i in range(5):
    message = "abc".encode('utf-8')
    debut = time.time()
    clientSocket.sendto(message, (ipServeur, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    fin = time.time()
    sum += fin-debut
    print(modifiedMessage.decode('utf-8'))
    print(f"RTT : ",fin-debut,"s")
print("Moyenne des RTT : ", sum, "s")
clientSocket.close()

# Probabilité de 0.5
# for i in range(5):
#     message = "abc".encode('utf-8')
#     delay = 0.1
#     if random.random() < 0.5:
#         while True:
#             clientSocket.settimeout(delay)
#             try:
#                 debut = time.time()
#                 clientSocket.sendto(message, (ipServeur, serverPort))
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


"""
Question 4 : Que se passe-t-il?

    Le client ne passera pas à la requête suivante tant que le serveur n'aura pas 
reçu une réponse pour la i-ème requête. Il va donc renvoyer la même requête au serveur un nombre limité de fois
puis passera, à la (i+1)ème requête. Si, la limite de tentatives est dépassée, le client arrête de renvoyer la même requête 
au serveur car ce dernier est possiblement "éteint".
"""