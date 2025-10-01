from socket import *
from threading import Thread
from pathlib import Path

def get_txt(test):
    with open(test, 'rb') as f:
        return f.read().decode('utf8')

serverPort = 1234
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(10)
print('server ready')

def handle_client(connectionSocket, addr):
    try:
        message = connectionSocket.recv(1024).decode()
        print("message : ", message, " de ", addr)

        """Prompt : comment extraire le chemin d'une requête HTTP en python ?"""
        path = message.split('\n')[0].split(' ')[1]
        fich = path.lstrip('/')
        fichier = Path(fich)

        if fichier.is_file():    
            content = get_txt(fichier)

            rep = 'HTTP/1.1 200 OK\r\n'
            rep += 'Server: BaseHTTP/0.6 Python/3.4.3\r\n'
            rep += 'Content-Type: text/xml\r\n'
            rep += f'Content-Length: {len(content)}\r\n\r\n'
            connectionSocket.sendall(rep.encode('utf-8') + content.encode('utf-8'))

        else:
            rep = 'HTTP/1.1 404 Not Found\r\n\r\n'
            msg_error = '404 Not Found'
            connectionSocket.sendall(rep.encode('utf-8') + msg_error.encode('utf-8'))
        connectionSocket.close()

    except Exception as e:
        print(e)
        connectionSocket.close()
    
#multithreading
while True:
    connectionSocket, addr = serverSocket.accept()
    Thread(target=handle_client, args=(connectionSocket, addr)).start()