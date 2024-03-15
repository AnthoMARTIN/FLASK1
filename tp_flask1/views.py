import socket
import threading

# C'est pour gérer les messages entrants
def handle_client(client_socket, address):
    while True:
# C'est la récéption des données du client
        data = client_socket.recv(12345).decode('utf-8')