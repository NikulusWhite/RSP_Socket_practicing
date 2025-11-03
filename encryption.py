import math
import random


class Encryptor():
    def __init__(self, text, e, n):
        self.text = text
        self.e = e  
        self.n = n  
    def encryption(self):
        encrypted_text = []

        for i in self.text:
            m = ord(i)
            c = pow(m, self.e, self.n)
            encrypted_text.append(c)
        encrypted_text_str = str(encrypted_text) + '\n'
        with open('encrypted text.txt', 'w')as f:
            for el in encrypted_text:
                letter = str(el) + '\n'
                f.write(letter)
        return encrypted_text
class Decryptor:
	c =[]
	def __init__(self):
		pass

	def decryption(self, c, d, n):
		self.c = c
		self.d = d  
		self.n = n 
		orig = pow(self.c, self.d, self.n)
		return chr(orig)
	

