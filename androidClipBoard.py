import androidhelper

droid = androidhelper.Android()

TCP_IP = droid.dialogGetInput().result

def sendText(text):
	import socket
	
	TCP_PORT = 5005
	BUFFER_SIZE = 1024
	MESSAGE = text
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(MESSAGE)
	data = s.recv(BUFFER_SIZE)
	s.close()
	

while(true):
	clipboard = droid.getClipboard()
	text = clipboard.text

	sendText(text)
	time.sleep(5)

