import socket
s=socket.socket()
host="127.0.0.1"
port=1221
s.connect((host,port))
s.send("Hello Server!!")

with open("recieved.txt","wb") as f:
    print "File opened"
    while 1:
        print "recieving data"
        data=s.recv(1024)
        if not data:
            break
        f.write(data)
f.close()
print("Download success")
s.close()
print("connection closed")
