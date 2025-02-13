import random

tam = 10
vetor = [0] * tam
for i in range(tam):
    vetor[i] = random.randint(1,40)

repetidos = []
for i in range(tam):
    for j in range(tam):
        if i != j and vetor[i] == vetor[j] and vetor[i] not in repetidos:
            repetidos.append(vetor[i])

print(vetor) 
print(repetidos)