import random

# Numeros distintos e aleatorios
vetor = []

while len(vetor) < 6:
    valor = random.randint(1,60)
    if valor not in vetor:
        vetor.append(valor)
        

# Não posso tirar os valores do vetor original
vistos = []
for _ in range(len(vetor)):
    # Definir qual é o menor valor do vetor
    for k in vetor:
        if k not in vistos:
            menor = k
            break

    for j in range(len(vetor)):
        if vetor[j] < menor and vetor[j] not in vistos:
            menor = vetor[j]
    
    vistos.append(menor)
    print(menor)
    