# echo_client.py
import socket

host = input("Enter host: ")   
port = int(input("Enter port: ") )                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print('Received', repr(data))
