from encryption import Encryptor
import random
import os

m = input('Enter text for encryption: ')
with open('open_key.txt', 'r') as f:
   	lines = f.readlines()
   	e = int(lines[0])
   	n = int(lines[1])
   	crypt = Encryptor(m, e, n)
   	crypt.encryption()
print('Text has been encrypted')
os.system('pause')