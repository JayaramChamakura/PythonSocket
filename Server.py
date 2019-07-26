# load additional Python module
import socket
import logging
from datetime import datetime
logging.basicConfig(filename='app.log', filemode='a+',format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)

class CustomSocket:
	def __init__(self,hostname,port):
		self.hostname = hostname
		self.port = port
	def createSock(self):
        	# create TCP/IP socket
        	self.ssock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        	# get the according IP address
        	ip_address = socket.gethostbyname(self.hostname)
        	# bind the socket to the port 23456
        	server_address = (ip_address, self.port)
        	print ('starting up on %s port %s' % server_address)
        	self.ssock.bind(server_address)
        	return self.ssock
	def recvData(self,connection,client_address):
		try:
			# show who connected to us
			#print (now,"-", client_address)
			recv_data=''
			# receive the data in small chunks and print it
			while True:
				chunk_data = connection.recv(64)
				if chunk_data:
					# output received data
					chunk_data=chunk_data.decode('utf-8')
					recv_data +=chunk_data
				else:
					# no more data -- quit the loop
					print ("data received:",recv_data)
					logging.info("[%s] - [%s]",client_address[0], recv_data)
					break
		finally:
			# Clean up the connection
			connection.close()
		return recv_data
	def listenClient(self):
		self.ssock.listen(1)

		while True:
			# wait for a connection
			print ('waiting for incoming connections')
			connection, client_address = self.ssock.accept()
			print ("-", client_address)
			data=self.recvData(connection,client_address)
			

def main():
	socketObj=CustomSocket('cineserver',11001)
	print(socketObj.hostname)
	socketObj.createSock()
	print (socketObj.ssock.getsockname())
	socketObj.listenClient()

if __name__ == "__main__":
	main()


