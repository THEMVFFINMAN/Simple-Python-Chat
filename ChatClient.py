import socket

# Put the Server host here
HOST = 'HOST IP ADDRESS GOES HERE'
# Put the server port here
PORT = 50011

# Create the socket and connect it to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Wait for input, print out what the server sends, etc
while 1:
    s.sendall(raw_input('>> '))
    data = s.recv(1024)
    print '> ', repr(data)
    
s.close()


