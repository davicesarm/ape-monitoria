""" Q1 - Leia 3 notas de um aluno, calcule a média com base nas duas maiores notas. Após isso, determine qual seria o conceito do aluno com base na tabela abaixo. Deve ser impresso a media, o conceito e, caso o conceito tenha sido A,B ou C, deve ser impresso que o aluno foi aprovado, caso contrário, reprovado.

media > 0 e <= 39: E
media > 40 e <= 59: D
media > 60 e <= 79: C
media > 80 e <= 89: B
media > 90 e <= 100: A
"""

n1,n2,n3 = map(int, input().split())

if n1 < n2 and n1 < n3:
    media = (n2 + n3) / 2
elif n2 < n3:
    media = (n1 + n3) / 2
else:
    media = (n1 + n2) / 2
    
