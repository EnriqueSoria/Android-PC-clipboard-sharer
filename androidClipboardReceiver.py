import socket
import time

TCP_IP = '192.168.1.3'
TCP_PORT = 6006
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)


while True:
	conn, addr = s.accept()
	print 'Connection address:', addr
	data = conn.recv(BUFFER_SIZE)
	if data:
		print data
		conn.send('ok')
		conn.close()
