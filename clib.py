import socket
from datetime import datetime
HOST = "localhost"
PORT = 4000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

while 1:
	
	message = input("Your Message: ")
	sock.send(bytes(message,'UTF-8'))
	if (message == '#QUEHORAS'):
		print ("As horas são:")
	elif (message == '#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (message == '#REGISTRAR'):
		print ("Qual o nome?")
		


sock.close()
