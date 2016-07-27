import socket
s=socket.socket()
host="127.0.0.1"
port=1221
s.bind((host,port))
s.listen(5)
print "Server running....."
while 1:
        conn,addr=s.accept()
        print "Got connection from "+(str)(addr)
        data=conn.recv(1024)
        print ("Server recieved:",repr(data))

        filename="send.txt"
        f=open(filename,'rb')
        l=f.read(1024)
        while l:
            conn.send(l)
            print ("Sent:",repr(l))
            l=f.read(1024)
        f.close()

        print "Done Sending....."
        conn.close()
    
