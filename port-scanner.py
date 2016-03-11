import socket,sys
ip=raw_input("Enter ip to scan:")
port=input("Enter port number:")
if port>65535:
    print("port number out of range")
    sys.exit()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((ip,port))
if result == 0:
    print "Port is open"
else:
    print "nope"
