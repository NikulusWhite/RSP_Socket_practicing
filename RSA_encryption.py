import math
import random
import numpy as np

m = str(input('Enter the message: '))

#чет на математическом
def is_prime(num):
    # 1. Простые числа должны быть больше 1
    if num <= 1:
        return False
    # 2. Проверяем делимость до квадратного корня числа
    # Достаточно проверять только до sqrt(num), так как если есть делитель больше sqrt(num),
    # то обязательно найдется и меньший делитель
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            # Если делится без остатка, то число не простое
            return False
    # Если делителей не найдено, число простое
    return True


def key_creation(p, q):
    n = p * q  
    
    f_n = (p - 1) * (q - 1)
    
    while True:
        e = random.randint(2, f_n - 1)
        if math.gcd(e, f_n) == 1:
            break
    print("Open key {", e," , ", n, "}")

    d =  pow(e, -1, f_n)
    d_str = str(d) + '\n'
    with open('open_key.txt', 'w')as f:
        f.write(str(e))
        f.write(str(n))
    
    with open('close_key.txt', 'w')as f:
        f.write(d_str)
        f.write(str(n))
    return e, n

def encryption(text, e, n):
    encrypted_text = []

    for i in text:
        m = ord(i)
        c = pow(m, e, n)
        encrypted_text.append(c)
    encrypted_text_str = str(encrypted_text) + '\n'
    with open('encrypted text.txt', 'w')as f:
        for el in encrypted_text:
            pinus = str(el) + '\n'
            f.write(pinus)
    return encrypted_text
            



prime_numbers=[]

with open('prime_numbers.txt', 'r') as f:
    for line in f:
        num = int(line.strip())
        prime_numbers.append(num)

    '''prime_numbers_no_np = (f.read())
prime_numbers = int(prime_numbers_no_np)
print(prime_numbers)
'''

#prime_numbers = np.loadtxt('prime_numbers.txt', dtype=int)

max_len = len(prime_numbers)
print(max_len, ' max_len')

random_number1 = random.randint(0,max_len - 1)
print(random_number1, ' random_number1')
random_number2 = random.randint(0,max_len - 1)
print('random_number2', random_number2)
if(random_number1 == random_number2):
    print('(Un)expected error. Please try again')
else:
    

    p = prime_numbers[random_number1]
    q = prime_numbers[random_number2]
    print('p ',p, 'q ', q)

    e, n = key_creation(p,q)


    encryption_process = encryption(m, e, n)
    print(encryption_process)




    '''for i in range(10000000,20000000):
    	if is_prime(i):
    		prime_numbers.append(i)
    '''

    #print(prime_numbers)
