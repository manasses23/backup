import socket
from datetime import datetime
HOST = "localhost"
PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

while 1:
	message = input("Your Message: ")
	sock.send(bytes(message,'UTF-8'))
	if (message == '#QUEHORAS'):
		data = sock.recv(1024)
		print (repr(data))
	elif (message == '#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (message == '#QUEDIA'):
		data = sock.recv(1024)
		print ("DATA:", repr(data))
	elif (message == '#LISTA'):
		data = sock.recv(1024)
		print ("LISTA:", repr(data))
	elif (message == '#REGISTRAR'):
		nome = input('Digite o nome do cliente para registrar\n')
		msg = nome.encode('utf-8')
		sock.send(msg)
	elif (message !="#QUEHORAS" or message !="#QUIT"or message!='#QUEDIA'or message!='#REGISTRAR'or message!='#LISTA'):
		data = sock.recv(1024)
		print ("ERRO:", repr(data))
	
sock.close()
