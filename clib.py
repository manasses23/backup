import socket
from datetime import datetime
HOST = "localhost"
PORT = 2000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

while 1:
	datahora = conn.recv(10240)
	data = repr(datahora)[2:-1]
	message = input("Your Message: ")
	sock.send(bytes(message,'UTF-8'))
	if (message == '#QUEHORAS'):
		print (data)
	elif (message == '#CLOSE_CONNECTION'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (message == '#CLOSE_CONNECTION'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break


sock.close()
