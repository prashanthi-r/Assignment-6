import socket
import pickle
from datetime import datetime

clientsocket= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
IP= "127.0.0.1"	# (input('Enter the IP Address of the server: ')).rstrip()
# PORT = (input('Enter the Port of the server: ')).strip()
PORT= 5005 # int(PORT)
clientsocket.connect((IP, PORT))

listofelements=[]
indices=[]
data=clientsocket.recv(1024)	# recieving list
listofelements=pickle.loads(data)
print(listofelements)

i=raw_input("Enter i: ")
j=raw_input("Enter j: ")

timestamp = datetime.now() # timestamp
indices.append(i)
indices.append(j)
indices.append(timestamp.year)
indices.append(timestamp.month)
indices.append(timestamp.day)
indices.append(timestamp.hour)
indices.append(timestamp.minute)
indices.append(timestamp.second)
indices.append(timestamp.microsecond)
indices_string= pickle.dumps(indices)	# sending indices and timestamp
clientsocket.send(indices_string)
clientsocket.close()