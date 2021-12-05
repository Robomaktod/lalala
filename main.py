import socket
import threading
from cezar import myencode

name = input("Choose your name : ").strip()
while not name:
    name = input("Please write your name correct").strip()
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.0.107"  # "127.0.1.1"
port = 1013
client.connect((host, port))
client_num = '1'

def sending():
    while 1:
        messagesd = input()
        ncode = input('encode msg? \nyes \nno \n')
        if ncode == 'no':
            message_with_name = "n" + '1' + name + " : " + messagesd
            client.send(message_with_name.encode())
        elif ncode == 'yes':
            message_with_name = name + " : " + messagesd
            client.send(myencode('x' + '1' + message_with_name, 1).encode())
        else:
            print("ERROR")


def msg():
    while 1:
        message = client.recv(1024).decode()
        if client_num != message[1]:
            if message[0] == 'y':
                print(myencode(message, -1)[2:])
            elif message[0] == 'n':
                print(message[2:])


thread_send = threading.Thread(target=sending)
thread_receive = threading.Thread(target=msg)
thread_send.start()
thread_receive.start()