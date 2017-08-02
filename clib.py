import socket
from datetime import datetime
HOST = "localhost"
PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))

while 1:
	
	message = input("Your Message: ")
	sock.send(bytes(message,'UTF-8'))
	#if (message == '#QUEHORAS'):
	#	data = sock.recv(1024)
	#	sock.close
	#	print ("As horas são:", repr(data))
		
	if (message == '#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	#elif (message == '#REGISTRAR'):
	#	nome = input('Digite o nome do cliente ou digite CTRL+C para sair \n')
	#	byte_msg = nome.encode('utf-8')
	#	sock.send(byte_msg)
	#	print ("Qual o nome?")
		


sock.close()
