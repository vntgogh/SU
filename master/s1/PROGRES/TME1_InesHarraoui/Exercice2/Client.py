from socket import *
import time
from struct import *

serverName = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

temps_client = time.time()
print("temps client : ",temps_client," secondes")

clientSocket.send(pack('!d',temps_client))
temps_serv = clientSocket.recv(2048)
print("Temps serveur : ", unpack('!d',temps_serv)[0]," secondes")
diff = unpack('!d',temps_serv)[0] - temps_client

print("Différence temps client - temps serveur :", diff," secondes")
clientSocket.close()
