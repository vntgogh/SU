from socket import *
from threading import *
from struct import *

relaiPort = 1236

serverPort = int(input("Entrer le port du serveur : "))
serverName = str(input("Entrer l'adresse IP du serveur : "))
main_uri = str(input("Entrer une URI : "))

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #evite d'avoir l'erreur adresse déja utilisée 
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

def get_txt(test):
    with open(test, 'rb') as f:
        return f.read().decode('utf8')    

def handle_client(clientConnection, addrClient):
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    
    message = get_block(clientConnection).decode('utf-8')     
    print("message du client :", message,"\n")

    put_block(clientSocket, message.encode('utf-8'))
    print("message envoyé au serveur\n")

    reponse = get_block(clientSocket).decode('utf-8')
    print("réponse du serveur :", reponse,"\n")

    uri = message.split('\n')[0].split(' ')[1].strip() 
    with open('sniffer.log', 'a') as f:
        f.write(uri + " : "+ addrClient[0] + "\n")

    if reponse:
        with open('sniffer.log', 'a') as f:
            f.write(uri + " : " +addrClient[0] + "\n")

    put_block(clientConnection, reponse.encode('utf-8'))
    print("réponse envoyée au client\n")

    clientConnection.close()
    clientSocket.close()

    main_uri_clients =[]
    with open('sniffer.log', 'r') as f:
        for ligne in f:
            if main_uri in ligne:
                    if ligne.split(' : ')[1] not in main_uri_clients:
                        main_uri_clients.append(ligne.split(' : ')[1])
        print("Adresses clients ayant demandé l'URI " +main_uri + " : ")
    for client in main_uri_clients:
        print(client)

while True:
    clientConnection, address = serverSocket.accept()
    print("connexion client acceptée\n")
    Thread(target=handle_client, args=(clientConnection,address,)).start()