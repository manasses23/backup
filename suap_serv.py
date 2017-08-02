import socket

HOST = socket.gethostbyname('localhost')
PORT = 2000
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind((HOST,PORT))
tcp_server_socket.listen()
client, addr = tcp_server_socket.accept()
print('Conexão de:', addr)


while True:
 from urllib.request import Request, urlopen
 import json
 MATRICULA = client.recv(1024)
 if not MATRICULA: break
 TOKEN = client.recv(1024)
 if not TOKEN: break
 AUTHORIZATION = client.recv(1024)
 if not AUTHORIZATION: break

 req = Request('https://suap.ifrn.edu.br/api/v2/edu/alunos/{}/'.format(MATRICULA))
 req.add_header('Accept', 'application/json')
 req.add_header('X-CSRFToken', TOKEN)
 req.add_header('Authorization', AUTHORIZATION)        

 dados_byte = urlopen(req).read()  
 dados_txt = dados_byte.decode('utf-8')
 print(dados_txt)

client.close()
tcp_server_socket.close()
