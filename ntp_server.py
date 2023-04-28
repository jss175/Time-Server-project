import ntplib 
import socket
import pytz
from datetime import datetime,timezone
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
serverSocket.bind(("",65432));
serverSocket.listen();

while(True):
	(clientConnected,clientAddress) = serverSocket.accept()
	print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
	print("PLEASE SELECT THE TIMEZONE IN WHICH YOU WANT THE CURRENT TIME:")
	dataFromClient=clientConnected.recv(1024)
	print(dataFromClient.decode());
	decode_data=dataFromClient.decode()
	c=ntplib.NTPClient()
	tmezn=pytz.timezone(decode_data)
	response = c.request('pool.ntp.org',version=3)
	response.offset
	clientConnected.send(str(datetime.fromtimestamp(response.tx_time, tz=tmezn)).encode())
	print("The selected timezone has been used and sent to the client:")
	
	#(clientConnected,clientAddress) = serverSocket.accept()
	print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
	data2FromClient=clientConnected.recv(1024)
	print(data2FromClient.decode());
	print("This is the second request sent!!")
	print("The data from client is:",data2FromClient.decode())
	clientConnected.send('HELLLOOOOO'.encode())
	data='456:0:9';
	clientConnected.send(data.encode())







	