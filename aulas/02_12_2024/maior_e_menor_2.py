"""
Na Terra das Altitudes, existem montanhas e vales que variam em alturas extremas: alguns alcançam o céu, enquanto outros descem abaixo do nível do mar. Certo dia, o Guardião do Horizonte pediu sua ajuda para determinar qual é o ponto mais alto (a montanha mais alta) e o ponto mais baixo (o vale mais profundo) da região.

Se a altitude for 0, finish.
"""

maior = menor = int(input())

while maior != 0:
    n = int(input())
    
    if n == 0:
        break
    
    if n > maior:
        maior = n
        
    if n < menor:
        menor = n
    
    
print("Maior:", maior)
print("Menor:", menor)