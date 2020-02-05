
import socket
import helper_methods
import select
import sys

from thread import *

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) \

# If different length output message and exit
if len(sys.argv) !=3:
    print "Please input in following format: filename, IP address, Port Number"
    exit()

IP = str(sys.argv[1])
PORT = int(str(sys.argv[2]))
clients = []

# IP Validation
if not helper_methods.is_valid_ipv4_address(IP):
    if not helper_methods.is_valid_ipv6_address(IP):
        print "IP is invalid. \nExiting now...."
        exit()
#Port Validation
if not helper_methods.is_valid_port(PORT):
    print "Port is invalid. \nExiting now...."
    exit()

# Good to go message
print("Connecting using: \nIP: " + sys.argv[1] + "\nPort Number: " + sys.argv[2])

try:
    soc.bind((IP, PORT))
except:
    print "Error using provided IP or Port"

# 100 connections
soc.listen(100)

# Remove clients method
def remove(connection, clients):
    if connection in clients:
       clients.remove(connection)

# Basic content of chat.
def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!")
    while True:
        try:
            message = conn.recv(2048)
            if message:
                print "<" + addr[0] + "> " + message
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                # Remove if broken
                remove(conn)
        except:
            continue


while True:
    conn, addr = soc.accept()
    clients.append(conn)
    # prints the address of the user that just connected
    print addr[0] + " connected"
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()





