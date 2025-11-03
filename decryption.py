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