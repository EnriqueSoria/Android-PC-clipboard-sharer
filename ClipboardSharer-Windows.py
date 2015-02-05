'''
	PC (server) side.

	It receives data, and puts it into the clipboard.
	It needs: http://sourceforge.net/projects/pywin32/
'''
import socket
import time
import win32clipboard

def get_clipboard():
	''' Opens a clipbard and get the text '''
	win32clipboard.OpenClipboard()
	data = win32clipboard.GetClipboardData()
	win32clipboard.CloseClipboard()
	return data

def set_clipboard(text):
	''' Opens a clipboard and sets text to it '''
	win32clipboard.OpenClipboard()
	win32clipboard.EmptyClipboard()
	win32clipboard.SetClipboard(text.encode('utf-8'), win32clipboard.CF_TEXT)
	win32clipboard.SetClipboard(unicode(text), win32clipboard.CF_UNICODETEXT)
	win32clipboard.CloseClipboard()

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
		set_clipboard(data)
		print data
		conn.send('ok')
		conn.close()
