from socket import *
from struct import *

def recvall(sock, length):
    blocks = []
    while length:
        block = sock.recv(length)
        if not block:
            raise EOFError('socket closed with %d bytes left'' in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)

def client_web(ipServeur, serverPort, fich):
    clientSocket = socket(AF_INET, SOCK_STREAM)

    try:
        clientSocket.connect((ipServeur, serverPort))
        print("Connecté au serveur ",ipServeur,":",serverPort)

        message = f"GET /{fich} HTTP/1.1\r\nHost: {ipServeur}\r\n\r\n"

        clientSocket.sendall(message.encode('utf-8'))

        """Prompt : comment récupérer l'entièreté des données venant d'une réponse du serveur sous http"""
        rep = b"" 
        while True:
            data = clientSocket.recv(4096)
            if not data: #condition d'arret
                break
            rep += data

        print(rep.decode('utf-8'))
        clientSocket.close()

    except Exception as e:
        print(e)
        clientSocket.close()

ipServeur = gethostname()  
serverPort = 1234              
fich = 'bonjour.txt' 

client_web(ipServeur, serverPort, fich)
