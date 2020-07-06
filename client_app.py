#!/usr/bin/env python3
import socket

s = socket.socket()
print("Please enter the hostname of the server you want to connect:")
host = input()
port = 8080
s.connect((host, port))

name = input("Please enter your name : ")
print(" Connected to chat server",host)
s.send(name.encode())
contact_name = s.recv(1024)
contact_name = contact_name.decode()
print("")
print(contact_name, "is online ")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(contact_name, ":" ,message)
    print("")
    message = input("Please enter your message: ")
    message = message.encode()
    s.send(message)
    print("message sent\n")
    