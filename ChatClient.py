import socket

HOST = 'HOST IP ADDRESS GOES HERE'
PORT = 'Pick a port, I like things that end in 11, 50011'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while 1:
    s.sendall(raw_input('>> '))
    data = s.recv(1024)
    print '> ', repr(data)
    
s.close()


