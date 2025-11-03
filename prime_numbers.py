import math
prime_numbers = []
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


for i in range(10000000,20000000):
    	if is_prime(i):
    		prime_numbers.append(i)




with open('prime_numbers.txt', 'w') as f:
	for num in prime_numbers:
		f.write(str(num) + '\n')
