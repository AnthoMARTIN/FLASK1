import socket


serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345

# C'est la liaison du socket au port
serveur_socket.bind((host, port))

# On attend la connexion du client
serveur_socket.listen(1)

print("Le serveur écoute sur le port :", port)

# Ca accepte la connexion du client
client_socket, adresse = serveur_socket.accept()
print("Connexion depuis :", adresse)

while True:
    # C'est la récéption des données du client
    message = client_socket.recv(1024).decode()
    if not message:
        break
    print("Message reçu du client :", message)

# C'est la fermeture de la connexion
client_socket.close()