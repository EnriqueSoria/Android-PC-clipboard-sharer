import androidhelper
import socket

'''
	Android (client) side.

	Uses QPython (2.x)
'''


droid = androidhelper.Android()

# Let's know that IP
TCP_IP = droid.dialogGetInput().result

def sendText(text, ip, port=5005, buffer_size=1024):
	'''
		Creates a socket and send the text
	'''
	# Constants
	MESSAGE = text
	TCP_IP = ip
	TCP_PORT = port
	BUFFER_SIZE = buffer_size
	
	# Create a socket
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Connect to IP:PORT
	s.connect((TCP_IP, TCP_PORT))

	# Send that message
	s.send(MESSAGE)

	# Get reply
	data = s.recv(BUFFER_SIZE)

	# Close socket
	s.close()
	

while(true):
	clipboard = droid.getClipboard()
	text = clipboard.text

	sendText(text, ip)
	time.sleep(5)

