import time,socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host=socket.gethostname()
print host
port=1668
s.bind((host,port))
s.listen(5)
try:
    while 1:
        client,addr=s.accept()
        print "connected to "+ (str)(addr)
        c_time=time.ctime(time.time())+"\n"
        client.send(c_time.encode("ascii"))
        client.close()
except:
    s.close()
