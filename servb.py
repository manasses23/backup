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
	login =str(datahora)+";"+" Ip:"+str(addr[0]+ "   \n" )
	logg= open('log.json','w')
	json.dump(login,logg,indent=4)
	logg.close
	logg=open('log.json')
	log=json.load(logg)
	registro=[]
	arq = open('/tmp/lista.txt', 'w' )
	registro.append(log)
	arq.writelines(registro ) 
	arq = open('/tmp/lista.txt', 'r')
	registro = arq.readlines()
	arq.close
	
	raw_data = conn.recv(1024)
	data = repr(raw_data)[2:-1]
	print(data)
	if (data == '#QUEHORAS'):
		hora = "HORA: hora é:",str (datahora.hour)+':'+ str(datahora.minute) +':'+ str(datahora.second)
		#byte_msg = bytes(hora('utf-8')
		#conn.send(byte_msg)
		print (hora)	

	elif (data =='#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (data =='#REGISTRAR'):
		print ("Digite o nome")
	elif (data =='#QUEDIA'):
		print ("DATA: ",str(datahora.day) +'/'+ str(datahora.month) +'/'+ str(datahora.year))
	elif (data =='#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break	
	elif (data =='#LISTA'):
		print (registro)
	elif (data !="#QUEHORAS" or data !="#CLOSE_CONNECTION"or data!='#QUEDIA'or data!='#REGISTRAR'or data!='#LISTA'):
		print ("FAULT 512")
conn.close()
