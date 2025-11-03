from encryption import Encryptor, Decryptor
from key_generator import KeyGen
import random

start = input("Generate new keys?(Y/N): ")
if (start == 'Y'):
	print("Generation... Please wait")
	prime_numbers=[]

	with open('prime_numbers.txt', 'r') as f:
		for line in f:
			num = int(line.strip())
			prime_numbers.append(num)

	max_len = len(prime_numbers)
	
	random_number1 = random.randint(0,max_len - 1)
	random_number2 = random.randint(0,max_len - 1)


	if (random_number1 == random_number2):
	    print('(Un)expected error. Please try again')
	else:
		p = prime_numbers[random_number1]
		q = prime_numbers[random_number2]
		kg = KeyGen(p,q)
		kg.key_creation()
		print('Keys have been generated')


else:
	print('WARNING Old keys are used!')

text = input('Initiate encryption or decryption process?(E/D): ')

if text == 'E':
	m = input('Enter text for encryption: ')
	with open('open_key.txt', 'r') as f:
	   	lines = f.readlines()
	   	e = int(lines[0])
	   	n = int(lines[1])
	   	crypt = Encryptor(m, e, n)
	   	crypt.encryption()
else:
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