"""
    1. Send a message to yourself by running both server and receiver
    2. Change the content of the message
    3. Change the IP address of the message to target a friend's computer
    4. Make it so that you can use the input() function to send a message
    5. Make it so that this server can also receive, meaning your friend
        can send a message TO YOU
        
"""

import socket
from time import sleep

UDP_IP = "127.0.0.1" # IP address to listen on
UDP_PORT = 5005  # Port to listen on

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.bind((UDP_IP, UDP_PORT)) # start listening
sock.settimeout(1)
print('Listening!')

while True:
    try:
        # Receive a total of 1024 bytes, then reset
        data, addr = sock.recvfrom(1024)
        data = data.decode('utf-8')  # turn into a "normal string", not bytes
        print("Received message >>", data)

    except socket.timeout:
        # More than one second passed since we got a communication!
        print('...Still Listening...')
