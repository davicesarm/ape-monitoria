""" Faça um programa que mostre 
todos os números primos de 1 a N 
(obs: N será lido) """

n = int(input())

for num in range(2, n + 1):
    eh_primo = True
    
    if num <= 1:
        eh_primo = False
    elif num <= 3:
        eh_primo = True
    elif num % 2 == 0 or num % 3 == 0:
        eh_primo = False
    else:
        for i in range(5, int(num ** 0.5) + 1, 6):
            if (num % i == 0) or (num % (i + 2) == 0):
                eh_primo = False
                break
    
    if eh_primo:
        print(num)
    