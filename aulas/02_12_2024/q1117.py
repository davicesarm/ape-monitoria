""" Faça um programa que leia varias notas referentes às avaliações de um aluno. Calcule e imprima a média das notas e qual foi a maior e a menor nota (por algum motivo, podem ter notas negativas kkk). Se a nota for 0, o programa para.
"""

soma_das_notas = 0
qtd_notas = 0

maior = menor = int(input("Nota: "))
soma_das_notas = soma_das_notas + maior
qtd_notas = qtd_notas + 1

while maior != 0:
    n = int(input("Nota: "))
    
    if n == 0:
        break
    
    if n > maior:
        maior = n
        
    if n < menor:
        menor = n
        
    soma_das_notas = soma_das_notas + n
    qtd_notas = qtd_notas + 1
        
    
print("Maior:", maior)
print("Menor:", menor)
print("Media:", soma_das_notas/qtd_notas)