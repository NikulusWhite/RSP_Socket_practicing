import math
import random


class Encryptor():
    def __init__(self, e, n):
        self.e = e  
        self.n = n  
    def encryption(self, text):
        self.text = text  
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
        return str(encrypted_text)

