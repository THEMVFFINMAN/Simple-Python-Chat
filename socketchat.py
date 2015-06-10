import socket

HOST = ''
PORT = 50011

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    conn.sendall(raw_input('> '))
    data = conn.recv(1024)
    print '> ', repr(data)
conn.close()
