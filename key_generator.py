import math
import random

class KeyGen:
    def __init__(self, p, q):
        self.p = p  
        self.q = q
    def key_creation(self):
        n = self.p * self.q  
        
        f_n = (self.p - 1) * (self.q - 1)
        
        while True:
            e = random.randint(2, f_n - 1)
            if math.gcd(e, f_n) == 1:
                break

        d =  pow(e, -1, f_n)
        
        self.e = e
        self.d = d 
        self.n = n
        
        with open('open_key.txt', 'w')as f:
            f.write(str(e) + '\n')
            f.write(str(n))
        
        with open('close_key.txt', 'w')as f:
            f.write(str(d) + '\n')
            f.write(str(n))
