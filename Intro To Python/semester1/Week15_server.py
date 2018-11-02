"""

    Challenges:

        1. Send a message to yourself by running both server and receiver
        2. Change the content of the message
        3. Change the IP address of the message to target a friend's computer
        4. Make it so that you can use the input() function to send a message
        5. Make it so that this server can also receive, meaning your friend
            can send a message TO YOU

"""
import socket

UDP_IP = "127.0.0.1"  # IP address
UDP_PORT = 5005  # Port
MESSAGE = "You've been hacked! This is yourself"  # Message to send

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

# Open an internet socket utilizing SOCK_DGRAM which means UDP

while True:
    MESSAGE = input()
    with socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) as conn:
        conn.sendto(bytes(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
