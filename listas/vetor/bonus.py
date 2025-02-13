""" 
A partir de um vetor A e vetor B de mesmo tamanho,
concatene-os para formar um vetor C sem repeticoes 
"""

a = [2, 3, 5]
b = [1, 3, 4]

c = []

for i in range(len(a)):
    if b[i] not in c:
        c.append(b[i])

    if a[i] not in c:
        c.append(a[i])
        
print(c)