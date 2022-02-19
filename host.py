import socket
import sys
import time

s = socket.socket()  # Here we have created a variable that will define a socket

host = socket.gethostname() # Here we have created a host and we will get the hostname

print("Server will start on host: ", host)

port = 1234
s.bind((host,port)) # Here we have to bind port with the host

print("Server is Bound Successfully")
s.listen(1) # We want our system to listen to only one server

conn, addr = s.accept() # This will basically accept the server to connect to the host

print(addr, "has connected")

while 1: # This while is for continuous Message Application
    message = input(str("You:>>"))  # Here we will type the message that we want to send to the receiver
    message = message.encode() # here our message will get encode for the cpu and it will again store it into the message variable.
    conn.send(message) # Here conn will send our message to the server
    incoming_message = conn.recv(1024) #here server will receive our message
    incoming_message = incoming_message.decode() # here our message will get decoded by the sys
    print("Client:>>",incoming_message) # Here we will be printing the client message

