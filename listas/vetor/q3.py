import random

vetor = []

while len(vetor) < 6:
    valor = random.randint(1,60)
    if valor not in vetor:
        vetor.append(valor)
        
print(vetor)