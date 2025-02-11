# len(lista) -> Tamanho de uma lista (ou string)

# for i in range(len(lista)):
#     print(f"Indice = {i}|Elemento = {lista[i]}")

# for elemento in lista: 
#     print(elemento)

import random
numero_aleatorio = random.randint(0, 20)

lista = []

while True:
    if len(lista) == 10:
        break    

    numero = random.randint(0, 100)
    
    if numero > 20 and numero < 60:
        lista.append(numero)
        
print(lista)