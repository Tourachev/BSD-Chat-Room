import socket
import select
import sys
import helper_methods

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if len(sys.argv) != 3:
    print "Please input in following format: filename, IP address, Port Number"
    exit()

IP = str(sys.argv[1])
PORT = int(str(sys.argv[2]))

# IP Validation
if not helper_methods.is_valid_ipv4_address(IP):
    if not helper_methods.is_valid_ipv6_address(IP):
        print "IP is invalid. \nExiting now...."
        exit()
#Port Validation
if not helper_methods.is_valid_port(PORT):
    print "Port is invalid. \nExiting now...."
    exit()

soc.connect((IP, PORT))

while True:
    soclist = [sys.stdin, soc]
    read,write,error = select.select(soclist, [], [])

    for socks in read:
        if socks == soc:
            message = socks.recv(2048)
            print message
        else:
            message = sys.stdin.readline()
            soc.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
soc.close()