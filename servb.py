import socket
from datetime import datetime
import json
HOST = "" 
PORT = 3000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
print("Connected by ", str(addr))

while 1:
	datahora = datetime.now()
	login =str(datahora)+";"+" Ip:"+str(addr[0] )
	logg= open('log.json','w')
	json.dump(login,logg,indent=4)
	logg.close
	logg=open('log.json')
	log=json.load(logg)
	raw_data = conn.recv(1024)
	data = repr(raw_data)[2:-1]
	print(data)
	if (data == '#QUEHORAS'):
		hora = "HORA:",str(datahora.hour)+':'+ str(datahora.minute) +':'+ str(datahora.second)
		hora1=str(hora)
		conn.send(bytes(hora1,'UTF-8'))
		print (hora)	
	elif (data =='#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (data =='#REGISTRAR'):
		registro=[]
		cliente = conn.recv(1024)
		reg = "Cliente:"+str(cliente)+"  Data/Hora:"+str(datahora)+" Ip:"+str(addr[0] )
		arq = open('/tmp/lista.txt', 'w' )
		registro.append(reg)
		arq.writelines(registro) 
		arq = open('/tmp/lista.txt', 'r')
		registro = arq.readlines()	
		arq.close
	elif (data =='#QUEDIA'):
		d= ("DATA: ",str(datahora.day) +'/'+ str(datahora.month) +'/'+ str(datahora.year))
		dia=str(d)
		conn.send(bytes(dia,'UTF-8'))
	elif (data =='#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break	
	elif (data =='#LISTA'):
		reg=str(registro)
		conn.send(bytes(reg,'UTF-8'))
	elif (data !="#QUEHORAS" or data !="#QUIT"or data!='#QUEDIA'or data!='#REGISTRAR'or data!='#LISTA'):
		erro=("FAULT 512")
		conn.send(bytes(erro,'UTF-8'))
		print (erro)
conn.close()
