import socket
HOST = socket.gethostbyname('localhost')
PORT = 3000
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_client_socket.connect((HOST,PORT))

cliente = tcp_client_socket.recv(1024)
while True:
 nome = input('Digite o nome do cliente ou digite CTRL+C para sair \n')
 byte_msg = nome.encode('utf-8')
 tcp_client_socket.send(byte_msg)
   	   
