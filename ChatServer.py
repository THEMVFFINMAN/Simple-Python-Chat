import socket

# Host is empty
HOST = ''
# Any port you pick will do
PORT = 50011

# Start the socket, bind it, and listen
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

# Set it to accept and print out when the client connects
conn, addr = s.accept()
print 'Connected by', addr

# Wait for input and print it out what the client sends
while 1:
    conn.sendall(raw_input('> '))
    data = conn.recv(1024)
    print '> ', repr(data)
conn.close()
