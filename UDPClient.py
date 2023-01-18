#UDP ChatApp client
#Author: Vhuhwavho Mokoma

import socket
import threading


port = 18000
client_address = "127.0.0.1"
ServerAddressPort = (client_address,port)
buffersize = 2048

def signup():
    print("***SIGN UP***")
    useremail = input("Enter your username: \n")
    password = input("Enter your password: \n")
    msgToServer = useremail + "," + password+":"+client_address
    UDPClientSocket.sendto(msgToServer.encode(),ServerAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(buffersize)
    msg = msgFromServer[0].decode()
    print(msg)

def login():
    print("***LOG-IN***")
    usrname = input("Enter your username: \n")
    password = input("Enter your password: \n")
    msgToServer = usrname + "," + password+":"+client_address+"\n"
    UDPClientSocket.sendto(msgToServer.encode(),ServerAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(buffersize)
    msg = msgFromServer[0].decode()
    print(msg)
    print("CHATAPP: "+usrname)

def chat():
    contact = input("Enter username of Contact you wish to Chat with:\n")
    UDPClientSocket.sendto(contact.encode(),ServerAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(buffersize)
    contactmsg = msgFromServer[0].decode()
    print(contactmsg[contactmsg.find("|")+1:])
    print("Enter message or Enter Q to quit")


def send():
    while True:
        ms = input()
        if ms == "Q":
            break
        UDPClientSocket.sendto(ms.encode(),ServerAddressPort)
        
def receive():
    while True:
        msg = UDPClientSocket.recvfrom(buffersize)
        print(">> " + msg[0].decode())
      


# Create a UDP socket at client
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

print("***Welcome to the ChatAPP***")
print("Do You have an existing Account? (Y/N)\n")
existingAcc = input()
if(existingAcc=="N"):
    choice = "N"
    UDPClientSocket.sendto(choice.encode(),ServerAddressPort)
    signup()
    
else:
    choice = "Y"
    UDPClientSocket.sendto(choice.encode(),ServerAddressPort)
    login()
    chat()
    while True:
        x1 = threading.Thread(target = send)
        x2 = threading.Thread(target = receive)
        x1.start()
        x2.start()



