import socket
from datetime import datetime
import json
HOST = "" 
PORT = 4000

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

	raw_data = conn.recv(10240)
	data = repr(raw_data)[2:-1]
	print(data)
	if (data == '#QUEHORAS'):
		print ("A hora é:",str(datahora.hour)+':'+ str(datahora.minute) +':'+ str(datahora.second))

	elif (data =='#QUIT'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (data =='#REGISTRAR'):
		print ("Digite o nome")
		 
	elif (data =='#QUEDATA'):
		print ("A data é:",str(datahora.day) +'/'+ str(datahora.month) +'/'+ str(datahora.year))
	         
		 
	elif (data !="#QUEHORAS" or data !="#CLOSE_CONNECTION"or data!='#QUEDATA'or data!='#REGISTRAR'or data!='#LISTA'):
		print ("FAULT 512")
conn.close()
