#!/usr/bin/python
import socket,sys
def find_service_name(host):
    for port in range(1,65535):
        try:
            s=socket.socket()
            if s.connect_ex((host,port))==0:
                print "Port: %s => service name: %s" %(port, socket.getservbyport(port, 'tcp'))
                #print "Port: %s => service name: %s" %(port, socket.getservbyport(port, 'udp'))
                s.close()
        except KeyboardInterrupt:
            sys.exit()
        except:
            continue
    
if __name__ == '__main__':
    if len(sys.argv)!=2:
        print "Usage: ./nmap.py <ip>"
        sys.exit()
    host=sys.argv[1]
    find_service_name(host)
