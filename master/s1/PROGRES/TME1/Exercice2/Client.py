from socket import *
from datetime import datetime

serverName = gethostname()
serverPort = 1234
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

FMT = '%Y-%m-%d %H:%M:%S.%f'
client_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

clientSocket.send(client_time.encode('utf-8'))
server_time = clientSocket.recv(2048).decode('utf-8')

client_time_dt = datetime.strptime(client_time, FMT)
server_time_dt = datetime.strptime(server_time, FMT)
print("temps client : ", client_time_dt)
print("temps serveur : ", server_time_dt)

diff = (server_time_dt - client_time_dt).total_seconds()

print("Différence temps client et temps serveur :", diff)
clientSocket.close()
