import socket
host="bootstrap"
port=1668
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
time=s.recv(1024)
s.close()
print time
