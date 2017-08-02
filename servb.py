import socket
from datetime import datetime
import json
HOST = "" 
PORT = 2000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)
conn, addr = sock.accept()
print("Connected by ", str(addr))

while 1:
	datahora = datetime.now()
	login =" Data/Hora:"+";"+str(datahora)+";"+" Ip:"+str(addr[0]+ "   \n" )
	logg= open('log.json','w')
	json.dump(login,logg,indent=4)
	logg.close
	logg=open('log.json')
	log=json.load(logg)

	raw_data = conn.recv(10240)
	data = repr(raw_data)[2:-1]
	print(data)
	if (data == '#QUEHORAS'):
		datahora = conn.send(10240)
		data = repr(datahora)[2:-1]
		print (datahora)
	elif (data =='#CLOSE_CONNECTION'):
		print ("CONNECTION_WILL_BE_CLOSED")
		break
	elif (data !="#QUEHORAS" or data !="#CLOSE_CONNECTION"or data!='#REGISTRAR'or data!='#REGISTRAR'or data!='#LISTA'):
		print ("FAULT 512")
conn.close()
