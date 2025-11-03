import math
import numpy as np
import random

def decryption(c,d,n):
	orig = pow(c, d, n)
	return chr(orig)

with open('close_key.txt', 'r') as f:
	lines = f.readlines()
	d = int(lines[0])
	n = int(lines[1])
c =[]

with open('encrypted text.txt', 'r') as f:
	for line in f:
		number = int(line.strip())
		c.append(number)



text = []

for i in range(len(c)):
	letter = decryption(c[i],d,n)
	text.append(letter)

print("".join(text))
