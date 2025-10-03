from socket import *
from threading import Thread
from pathlib import Path
from struct import *

header_struct = Struct("!I")
def put_block(sock, message):
    block_length = len(message)
    sock.sendall(header_struct.pack(block_length))
    sock.sendall(message)

def get_txt(test):
    with open(test, 'rb') as f:
        return f.read().decode('utf8')

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('server ready')

def handle_client(connectionSocket, addr):
    message = connectionSocket.recv(1024).decode()
    print("message : ", message, " de ", addr)

    fich = message.split('\n')[0].split(' ')[1] #recupere le 2eme mot de la 1ere ligne(fichier)
    fichier = Path(fich)

    if fichier.is_file():    
        contenu = get_txt(fichier)

        rep = "HTTP/1.1 200 OK\r\n"
        rep += "Server: BaseHTTP/0.6 Python/3.4.3\r\n"
        rep += "Content-Type: text/xml\r\n"
        rep += "Content-Length: "+str(len(contenu))+"\r\n\r\n"
        put_block(connectionSocket, (rep + contenu).encode('utf-8'))

    else:
        rep = 'HTTP/1.1 404 Not Found\r\n\r\n'
        msg_error = '404 Not Found'
        put_block(connectionSocket, (rep + contenu).encode('utf-8'))
    connectionSocket.close()

#multithreading
while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handle_client, args=(connectionSocket, addr)).start()