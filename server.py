
from socket import *

sock=socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_address = ('localhost', 5000)
print('Iniciando servidor en %s puerto %s' % server_address)
sock.bind(server_address)

sock.listen()

def server():

    print('Esperando conexión...')
    connection, client_address = sock.accept()
    print('Conexión desde ', client_address)

    while True:
           
            data = connection.recv(1600)
            print('received "%s"' % data)
            
            if data:
                print('Enviando datos devuelta al cliente')
                msg = str(data)
                msg = msg.upper() 
                msg = bytes(msg, 'utf-8')
                connection.sendall(msg)

            if not data:
                print('Finalizando servidor')
                connection.close()
                sock.close()
                break
        
server()
    
  
