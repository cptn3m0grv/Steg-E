import socket
import os 

def create_socket():
    try:
        global host 
        global port
        global s
        host=""
        port="7777"
        s=socket.socket()
    except socket.error as sag:
        print("error aa gayeya babu"+sag)

#binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print("binding the port and the port no"+str(port))
        s.bind(host,port)
    except socket.error as msg:
        

    

    
     
