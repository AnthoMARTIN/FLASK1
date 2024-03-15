import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 12345  # C'est le même port utilisé par le server

# C'est la connexion au serveur
client_socket.connect((host, port))

while True:
    # C'est la saisie du message à envoyer
    message = input("Entrez un message : ")

    # C'estv l'envoi du message au serveur
    client_socket.send(message.encode())

    # L'arrêt si l'utilisateur tape 'au revoir'
    if message.lower() == 'au revoir':
        break

# Fermeture de la connexion
client_socket.close()