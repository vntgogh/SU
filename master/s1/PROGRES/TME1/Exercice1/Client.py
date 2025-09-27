from socket import *
import time
import random

ipServeur = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(0.1)  # délai initial

for i in range(5):
    message = "abc".encode('utf-8')
    delay = 0.1
    if random.random() < 0.5:
        while True:
            clientSocket.settimeout(delay)
            try:
                debut = time.time()
                clientSocket.sendto(message, (ipServeur, serverPort))
                modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
            except timeout:
                delay *= 2
                if delay > 2.0:
                    raise RuntimeError('server seems down')
            else:
                fin = time.time()
                print(modifiedMessage.decode('utf-8'))
                print(f"RTT : ",fin-debut,"s")
                break

clientSocket.close()

"""
Question 4 : Que se passe-t-il?

    Le client ne passera pas à la requête suivante tant que le serveur n'aura pas 
reçu une réponse pour la i-ème requête. Il va donc renvoyer la même requête au serveur
il passera, alors, à la (i+1)ème requête. Sinon, le client arrête de renvoyer la même requête 
au serveur car ce dernier est possiblement "éteint".
"""