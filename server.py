
import socket
import helper_methods
import select
import sys

from thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) \

# If different length output message and exit
if len(sys.argv) !=3:
    print "Please input in following format: filename, IP address, Port Number"
    exit()

IP = str(sys.argv[1])
PORT = str(sys.argv[2])

# IP Validation
if not helper_methods.is_valid_ipv4_address(IP):
    if not helper_methods.is_valid_ipv6_address(IP):
        print "IP is invalid. \nExiting now...."
        exit()
#Port Validation
if not helper_methods.is_valid_port(PORT):
    print "Port is invalid. \nExiting now...."
    exit()

print("IP: " + sys.argv[1] + "\nPort Number: " + sys.argv[2])



