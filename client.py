#!/usr/bin/env python
# coding: utf-8


#needed for network accessing
import socket
#needed to take arguments
import sys

#default port
PORT = 27993
#variables to keep track of position in arguments
pflag = False
argno = 0
for arg in sys.argv:
    if arg == '-p':
        pflag = True
    elif pflag:
        PORT = int(arg)
        pflag = False
    else:
        if (argno == 1):
            HOST = arg
        if (argno == 2):
            ID_NO = arg
        argno += 1

print(PORT)
print(HOST)
print(ID_NO)

#set up socket s
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to servver
s.connect((HOST, PORT))
s.sendall(b'cs3700fall2020 HELLO ' + ID_NO.encode('utf-8') + b'\n')
response = s.recv(8192).decode('utf-8')
print(response)
#do as many FINDs as requested
while (response.split()[1] == 'FIND'):
    ch = response.split()[2]
    search = response.split()[3]
    numoccurences = search.count(ch)
    message = 'cs3700fall2020 COUNT ' + str(numoccurences) + '\n'
    s.sendall(message.encode('utf-8'))
    response = s.recv(8192).decode('utf-8')
print("LOOP ENDED")
print(response)
#close connection
s.close()    