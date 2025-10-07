from socket import *
from threading import *
from struct import *


relaiPort = 1235

serverPort = int(input("Entrer le port du serveur : "))
serverName = str(input("Entrer l'adresse IP du serveur : "))

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', relaiPort))
serverSocket.listen(5)
print('relai ready')

def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left''in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)

header_struct = Struct("!I")
def put_block(sock, message):
    block_length = len(message)
    sock.sendall(header_struct.pack(block_length))
    sock.sendall(message)

def get_block(sock):
    data = recvall(sock, header_struct.size)
    (block_length,) = header_struct.unpack(data)
    return recvall(sock, block_length)

def handle_client(clientConnection):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))

    raw_length = recvall(clientConnection, 4)
    message_length = unpack('!I', raw_length)[0]
    
    message = clientConnection.recvall(2048)
    print("message du client :", message.decode('utf-8'))
    clientSocket.send(message)
    print("message envoyé au serveur")
    
    reponse = clientSocket.recvall(2048)
    print("réponse du serveur :", reponse.decode('utf-8'))
    clientConnection.send(reponse)
    print("réponse envoyée au client")
    
    clientConnection.close()
    clientSocket.close()

while True:
    clientConnection, address = serverSocket.accept()
    print("connexion client acceptée")
    Thread(target=handle_client, args=(clientConnection,)).start()