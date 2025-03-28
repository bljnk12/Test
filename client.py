
from socket import *

sock=socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_address = ('localhost', 5000)
print('Conectando al %s puerto %s' % server_address)
sock.connect(server_address)


def cliente():

        while True:
                amount_received = 0
                message = input('Escribe tu mensaje: ')
                print('Enviando: "%s"' % message)
                sock.sendall(bytes(message, 'utf-8'))
                data = sock.recv(1600)
                amount_received += len(data)
                print('Recibido "%s"' % data)

                if message.rstrip() == 'DESCONEXION':
                        print('Finalizando cliente')
                        sock.close()
                        break
        

cliente()