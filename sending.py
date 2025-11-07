import socket
import random
from encryption import Encryptor


m = input('Enter text for encryption: ')
with open('open_key.txt', 'r') as f:
   	lines = f.readlines()
   	e = int(lines[0])
   	n = int(lines[1])
   	crypt = Encryptor(m, e, n)
   	crypt.encryption()
print('Text has been encrypted')


text_to_send = []

HOST = '0.0.0.0'
PORT = 22869

with open('encrypted text.txt', 'r') as f:
	for line in f:
		number = str(line.strip())
		text_to_send.append(number)

message = '\n'.join(text_to_send)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Connection established c: ', addr)
		#тут не нужен цикл, т.к. мы один раз отправляем, а не слушаем бесконечно
		conn.sendall(message.encode('utf-8'))
		data = conn.recv(65000)
		print('Client answer: ', data.decode('utf-8'))
