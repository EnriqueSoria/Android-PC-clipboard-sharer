import socket
import time

'''
	PC (server) side.

	It receives data, and puts it into the clipboard.
'''

def setTextToClipboard(text):
	# TODO
	
	return False

# Constants
TCP_IP = '192.168.1.3'
TCP_PORT = 6006
BUFFER_SIZE = 1024

# We create a socket server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:
	# Accept connection
	conn, addr = s.accept()

	# Log addres
	print 'Connection address:', addr

	# Receive data
	data = conn.recv(BUFFER_SIZE)

	# Process data
	if data:
		print data
		conn.send('ok')
		conn.close()
