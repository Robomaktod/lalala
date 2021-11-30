import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
ADDRESS = "0.0.0.0"
clients = []
server.bind((ADDRESS, PORT))
print("server start")

def accept():
    while True:
        server.listen()
        client, address = server.accept()
        clients.append(client)
        start_listenning_thread(client, address)



def start_listenning_thread(client, address):
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client, address,)  # the list of argument for the function
    )
    client_thread.start()


def listen_thread(client, address):
    while True:
        message = client.recv(1024).decode()
        if message:
            print(f"Received message : {message}")
            broadcast(message, address)
        else:
            print(f"client has been disconnected : {client}")
            clients.remove(client)
            return


def broadcast(message, address):
    for client in clients:
         client.send(message.encode())









accept()
