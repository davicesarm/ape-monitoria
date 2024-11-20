""" Um número é, por definição, 
primo se ele não tem divisores, 
exceto 1 e ele  próprio. 
Faça um programa que leia um número e 
determine se ele é ou não  primo.  """

n = int(input())

eh_primo = True

if n <= 1:
    eh_primo = False
elif n <= 3:
    eh_primo = True
elif n % 2 == 0 or n % 3 == 0:
    eh_primo = False
else:
    for i in range(5, int(n ** 0.5) + 1, 6):
        if (n % i == 0) or (n % (i + 2) == 0):
            eh_primo = False
            break
