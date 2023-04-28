import ntplib 
import socket
import pytz
from datetime import datetime,timezone
def main():
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
		serverSocket.bind(("",65432));
		serverSocket.listen();
		while(True):
			(clientConnected,clientAddress)=serverSocket.accept()
			print("Accepted a connection request from the client : %s %s"%(clientAddress[0],clientAddress[1]))
			dataFromClient=clientConnected.recv(1024)
			decode_data=dataFromClient.decode()
			str(decode_data)
			if decode_data == '1':
				selection(clientConnected)
			elif decode_data == '2':
				synchronization(clientConnected)
def selection(clientConnected):
		c=ntplib.NTPClient()
		decode_tmze=clientConnected.recv(1024)
		timezne=pytz.timezone(decode_tmze)
		response = c.request('pool.ntp.org',version=3)
		response.offset
		clientConnected.send(str(datetime.fromtimestamp(response.tx_time, tz=timezne)).encode())
		print("The response has been sent to the client")

def synchronization(clientConnected):
	c = ntplib.NTPClient()
	# Provide the respective ntp server ip in below function
	decode1=clientConnected.recv(1024)
	tmzne1=pytz.timezone(decode1)
	print("Colleage:1 is residing in ",tmzne1)
	decode2=clientConnected.recv(1024)
	tmzne2=pytz.timezone(decode2)
	print("Colleage:2 is residing in ",tmzne2)
	response = c.request('pool.ntp.org', version=3)
	response.offset
	tim1=datetime.fromtimestamp(response.tx_time,tz=tmzne1)
	tim2=datetime.fromtimestamp(response.tx_time,tz=tmzne2)
	t1=datetime.strptime(tim1.strftime("%H:%M:%S"),"%H:%M:%S")
	t2=datetime.strptime(tim2.strftime("%H:%M:%S"),"%H:%M:%S")
	if tim1 > tim2:
		diff=t1-t2
	else:
		diff=t2-t1
	diff2=str(diff)
	clientConnected.send(str(tim1).encode())
	clientConnected.send(str(tim2).encode())
	clientConnected.send(diff2.encode())
	print("The scheduled time events has been sent to the client")
if __name__ == '__main__':
		main()
	
			
	