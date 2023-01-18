#UDP ChatApp server
#Author: Vhuhwavho Mokoma

import socket
import threading

def send():
    while True:
        ms = input()
        UDPServerSocket.sendto(ms.encode(),address)

def receive():
   while True:
        msg = UDPServerSocket.recvfrom(bufferSize)
        print(">> " + msg[0].decode())
    



localIP = "127.0.0.1"
port = 18000
bufferSize = 2048


#socket created
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to IP and Address
UDPServerSocket.bind((localIP, port))

print("UDP server up and listening")


# Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = message.decode()

    if(clientMsg=="N"):
        clientData = UDPServerSocket.recvfrom(bufferSize)
        file1 = open("users.txt",'a+')
        file1.write(clientData[0].decode()+"\n")
        file1.close()
        msgToSend = "SIGN-UP SUCCESSFULL"
        UDPServerSocket.sendto(msgToSend.encode(), address)
    else:
        clientData = UDPServerSocket.recvfrom(bufferSize)
        file1 = open("users.txt",'r')
        userdata = clientData[0].decode()
        user_list = file1.readlines()
        msgToSend = "LOG-IN UNSUCCESSFULL"
        if (userdata in user_list):
            msgToSend = "LOG-IN SUCCESSFULL"
        file1.close()
        UDPServerSocket.sendto(msgToSend.encode(), address)

        contactReq = UDPServerSocket.recvfrom(bufferSize)
        
        correct_index = -1
        for n in range(len(user_list)):
            user = user_list[n]
            if(user[:user.find(",")]==contactReq[0].decode()):
               correct_index = n
        
        if(correct_index!=-1):
            usr = user_list[correct_index]
            msg = usr[usr.find(":")+1:]+"|Contact Available"
            UDPServerSocket.sendto(msg.encode(), address)
            while True:
                x1 = threading.Thread(target = send)
                x2 = threading.Thread(target = receive)
                x1.start()
                x2.start()
        else:
            msg = "0000J|Contact Unavailable"
            UDPServerSocket.sendto(msg.encode(), address)