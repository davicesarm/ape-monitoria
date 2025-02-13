import random

vetor = [0] * 10

for i in range(10):
    vetor[i] = random.randint(1,60)

tem_repeticao = False
for i in range(10):
    for j in range(10):
        if i != j and vetor[i] == vetor[j]:
            tem_repeticao = True
            break
    
    if tem_repeticao:
        break
    
    
print(vetor)
if tem_repeticao:
    print("Y")
else:
    print("N")