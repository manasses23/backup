import socket
HOST = socket.gethostbyname('localhost')
PORT = 3000
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen(0)

client, addr = tcp_server_socket.accept()
message = "Conectado"
byte_msg = message.encode('utf-8')
client.send(byte_msg)
registro = []
while True:
    cliente = client.recv(1024)
    if not cliente: break
    from datetime import datetime
    datahora = datetime.now()
    reg = "Cliente:"+str(cliente)+" Data/Hora:"+str(datahora)+" Ip:"+str(addr[0]+ "   \n" )
    arq = open('/tmp/lista.txt', 'w' )
    registro.append(reg)
    arq.writelines(registro ) 
    arq = open('/tmp/lista.txt', 'r')
    registro = arq.readlines()
    for linha in registro:
       print (linha )
    arq.close() 
client.close()
tcp_server_socket.close()
