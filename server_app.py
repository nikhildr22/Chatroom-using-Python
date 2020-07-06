#!/usr/bin/env python3
import socket

s = socket.socket()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host, port))

print("\nServer is waiting for incoming connections\n")
s.listen(1)
conn, addr = s.accept()
print("Connection was successfull\n")
name = input("Please enter your name: ")
contact_name = conn.recv(1024)
contact_name = contact_name.decode()
print(contact_name, "is online")
conn.send(name.encode())

while True:
    message = input("Please enter your message: ")
    conn.send(message.encode())
    print("Sent\n")
    message = conn.recv(1024)
    message = message.decode()
    print(contact_name, ":" ,message)
    print("")