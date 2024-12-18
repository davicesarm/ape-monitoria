lista = [15, 25, 1, 63, 57, 36, 25, 4, 68, 16]
lista2 = [1, 2, 3, 45]

for n in lista2:
    if n not in lista:
        lista.append(n)
        
print(lista)