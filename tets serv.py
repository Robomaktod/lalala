import socket, threading


class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT = 1010
        ADDRESS = "0.0.0.0"
        self.clients = []
        self.server.bind((ADDRESS, PORT))
        self.message = ''
        print("server start")

    def accept(self):
        while True:
            self.server.listen()
            self.client, self.address = self.server.accept()
            self.clients.append(self.address)
            start_listenning_thread(self.client)



    def start_listenning_thread(self, client):
        client_thread = threading.Thread(
            target=listen_thread,
            args=(client,)  # the list of argument for the function
        )
        client_thread.start()


    def listen_thread(self):
        while True:
            self.message = self.client.recv(1024).decode()
            if self.message:
                print(f"Received message : {self.message}")
                self.broadcast(self.message)
            else:
                print(f"client has been disconnected : {self.client}")
                self.clients.remove(self.client)
                return


    def broadcast(self):
        if self.message[1] == '2':
            self.client.sendto(self.message.encode(), )
            # elif message[1] == '1':
            #     self.client.send(message.encode())





    accept()
