import socket

UDP_IP = "127.0.0.1"  # IP address
UDP_PORT = 5005  # Port
MESSAGE = "Hello, World!"  # Message to send

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

# Open an internet socket utilizing SOCK_DGRAM which means UDP

while True:
    with socket.socket(socket.AF_INET,  socket.SOCK_DGRAM) as sock:
        sock.sendto(bytes(MESSAGE,'utf-8'), (UDP_IP, UDP_PORT))
