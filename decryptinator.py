from decryption import Decryptor
import os


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