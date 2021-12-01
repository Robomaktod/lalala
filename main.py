import socket
import threading
from cezar import myencode

name = input("Choose your name : ").strip()
while not name:
    name = input("Please write your name correct").strip()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"  # "127.0.1.1"
port = 2221
client.connect((host, port))


def thread_sending():
    while 1:
        messagesd = input()
        ncode = input('encode msg? \nyes \nno \n')
        if ncode == 'no':
            message_with_name = "n" + '1' + name + " : " + messagesd
            selector = "first"
            client.send(message_with_name.encode())
            client.send(selector.encode())
        elif ncode == 'yes':
            message_with_name = name + " : " + messagesd
            selector = "first"
            client.send(myencode('x' + '1' + message_with_name, 1).encode())
            client.send(selector.encode())


def thread_receiving():
    while True:
        message = client.recv(1024).decode()
        selector = client.recv(2048).decode()
        if message[0] == 'y':
            print(myencode(message, -1)[2:])
        elif message[0] == 'n':
            print(message[2:])


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
