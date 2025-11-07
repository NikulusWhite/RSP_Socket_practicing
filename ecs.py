import socket
import os
import random
from key_generator import KeyGen
from encryption import Encryptor
from decryption import Decryptor

HOST = str(input('Connect to(IPv4 address): '))
PORT = 22869

prime_numbers=[]

with open('prime_numbers.txt', 'r') as f:
	for line in f:
		num = int(line.strip())
		prime_numbers.append(num)

max_len = len(prime_numbers)
    
random_number1 = random.randint(0,max_len - 1)
random_number2 = random.randint(0,max_len - 1)
p = prime_numbers[random_number1]
q = prime_numbers[random_number2]

new_keys = KeyGen()
new_keys.key_creation(p, q)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Ожидаю клиента...")
    conn, addr = s.accept()
    print("Клиент подключился:", addr)

    with open('open_key.txt', 'r') as f:
    	lines = f.readlines()
    	e_to_send = lines[0]
    	n_to_send = lines[1]
    with open('close_key.txt', 'r') as f:
    	lines = f.readlines()
    	d = lines[0]
    	n = lines[1]
    with conn:
    	key_data = f"{e_to_send}|{n_to_send}"
    	conn.sendall(key_data.encode('utf-8'))

    	data = conn.recv(65000).decode('utf-8')
    	e_from_client, n_from_client = data.split("|")
    	decr = Decryptor()
    	enc = Encryptor(int(e_from_client), int(n_from_client))
    	while True:
            data = conn.recv(65000)
            data_to_decrypt = data.decode('utf-8')
            #ну безуслдовно важно знать, что тут возвращается стринг и надо теперь его перобразовать :/

            data_to_decrypt = data_to_decrypt.strip('[]')
            data_to_decrypt = data_to_decrypt.split(',')

            c = []
            for i in data_to_decrypt:
                c.append(int(i))
            fin = []
            for i in range(len(c)):
                letter = decr.decryption(c[i],d,n)
                fin.append(letter)
            print("".join(fin))

            msg = input('Server: ')
            enc_msg = enc.encryption(msg)
            print(enc_msg)
            conn.sendall(enc_msg.encode('utf-8'))


