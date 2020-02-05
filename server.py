
import socket
import help
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



print("IP: " + sys.argv[1] + "\nPort Number: " + sys.argv[2])



if not is_valid_ipv4_address(IP) or is_valid_ipv6_address(IP):
    print "fail"
    exit()
