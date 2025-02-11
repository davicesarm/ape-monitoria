numero = int(input())
maior = numero
posicao = 1

for i in range(2, 101):
    numero = int(input())
    
    if numero > maior:
        maior = numero
        posicao = i

print(maior)
print(posicao)
