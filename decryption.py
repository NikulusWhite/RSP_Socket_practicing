class Decryptor:

	def __init__(self):
		pass

	def decryption(self, c, d, n):
		self.c = int(c)
		self.d = int(d)  
		self.n = int(n) 
		orig = pow(self.c, self.d, self.n)
		return chr(orig)