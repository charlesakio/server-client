from socket import *

host = '142.55.107.217' #Server IP address

port = 5555 #This port will be bound in server
backlog = 5 #The backlog is the maximum number of queued connections
size = 1480

listensock = socket(AF_INET,SOCK_STREAM)
listensock.bind((host,port))
listensock.listen(backlog)
servercloseflag = False

while not servercloseflag:
 	print('Waiting for client connection...')
 	clientsock, clientaddress = listensock.accept()
 	print('Recieved connection from :', 
 			clientaddress[0], 
 			'on port: ',
			clientaddress[1])
 	recdata = clientsock.recv(size) #Receieved data of byte type
 	
 	file_name = recdata.decode()
 	file_data = ""
 	files = open(file_name)
 	for line in files:
 		file_data = file_data + (line) + '\n'


 	while recdata:
 		print('Received data from ', clientaddress[0], ': ',recdata.decode())
 		clientsock.send(file_data.encode()) #echo back (test only)
 		recdata= clientsock.recv(size)
 
 		if recdata.decode() == 'end' or recdata.decode() == 'quit': #close client first
 			print('Closing connection with ', clientaddress[0])
 			clientsock.close()
 			break
 
 	if recdata.decode() == 'quit': #Close server
 		servercloseflag = True

print('Closing server:')
listensock.close()
print('Bye...')

