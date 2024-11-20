""" Faça um programa que calcule e mostre o 
fatorial de um número N, fornecido  pelo usuário. 
"""

# 4 * 3 * 2 * 1

n = int(input())

fatorial = 1
for i in range(2, n + 1):
    fatorial = fatorial * i
    
print(fatorial)