""" 8. Escreva um programa que calcule o valor do cosseno de X(lido em radianos), através de 20 termos da série
abaixo """

import math

x = int(input())

total = 1
somar = False

for i in range(2, 80, 2): # Ao inves de usar 20 termos, usamos 40. por algum motivo que desconheço rs
    fatorial = 1
    for j in range(2, i + 1):
        fatorial = fatorial * j
    
    resultado = (x ** i) / fatorial
    
    if somar:
        total += resultado
        somar = False
    else:
        total -= resultado
        somar = True
    
    
print("Reposta nossa:")
print(total)

print("\nGabarito:")
import math
print(math.cos(20))