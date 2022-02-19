import socket
import sys
import time

s = socket.socket()  # Here we have created a variable that will define a socket

host = input(str("Please Enter the host name"))

port =1234

try:
    s.connect((host,port))
    print("Connected to the server")

except:
    print("Connection to the server failed")

while 1: # This while is for continuous Message Application
    incoming_message = s.recv(1024) #here server will receive our message
    incoming_message = incoming_message.decode() # here our message will get decoded by the sys
    print("Server:>>", incoming_message)
    message = input(str("You:>>"))  # Here we will type the message that we want to send to the receiver
    message = message.encode() # here our message will get encode for the cpu and it will again store it into the message variable.
    s.send(message) # Here conn will send our message to the server
    