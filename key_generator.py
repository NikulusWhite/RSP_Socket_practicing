import math
import random
import os

class KeyGen:
    def __init__(self):
        pass
    def key_creation(self, p, q):
        self.p = p  
        self.q = q
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

'''start = input("Generate new keys?(y/n): ")
if (start == 'y'):
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
os.system('pause')'''