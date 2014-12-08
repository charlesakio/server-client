#Client code
from socket import *

serverip = '142.55.107.217' #Use your server IP address here
serverport = 5555 #Use last 4 digits of your ID
datasize = 1024 #Note the double parenthesis (why?)

sock1 = socket(AF_INET,SOCK_STREAM)
sock1.connect((serverip,serverport))
close_flag = False

while not close_flag:
    data_Out = input('Enter file name ')
    if len(data_Out):
        sock1.send(data_Out.encode())
    if data_Out == 'end' or data_Out == 'quit':
        close_flag=True
    else:
        dataIn=sock1.recv(datasize)
        print('Received data from server: \n', dataIn.decode())
        download_file = open(data_Out, 'w') # Creates file
        file_input = dataIn.decode()
        download_file.write(file_input)
        download_file.close()

        print('File saved ' + data_Out)
print('Closing connection with server', serverip)
sock1.close()
