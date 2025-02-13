import random

tam = 10
vetor = [0] * tam
for i in range(tam):
    vetor[i] = random.randint(1, 60)

repetidos = []
for i in range(tam):
    for j in range(tam):
        if i != j and vetor[i] == vetor[j]:
            repetidos.append(vetor[i])

nao_repetidos = []
for i in vetor:
    if i not in repetidos:
        nao_repetidos.append(i)
        
print(vetor)
print(nao_repetidos)

