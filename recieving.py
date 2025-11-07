import socket
from decryption import Decryptor
import os

HOST = '127.0.0.1'
PORT = 22869

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	data = s.recv(65000)
	print('Получено от сервера:', data.decode('utf-8'))
	answer = 'message recieved!'
	s.sendall(answer.encode('utf-8'))
	to_decr = str(data.decode('utf-8'))
	with open('encrypted text.txt', 'w') as f:
		f.write(to_decr)


with open('close_key.txt', 'r') as f:
		lines = f.readlines()
		d = int(lines[0])
		n = int(lines[1])
decr = Decryptor()


c =[]
fin = []
with open('encrypted text.txt', 'r') as f:
	for line in f:
		number = int(line.strip())
		c.append(number)

for i in range(len(c)):
	letter = decr.decryption(c[i],d,n)
	fin.append(letter)
print("".join(fin))
os.system('pause')