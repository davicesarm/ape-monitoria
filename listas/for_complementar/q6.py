""" Escreva um programa que gere um triângulo 
de asteriscos, com o tamanho de linhas
informado pelo usuário. Por exemplo,
para a quantidade de de linhas igual a 6,
a saída deverá ser: 

*
**
***
****
*****
******

"""

qtd_linhas = int(input())

if qtd_linhas < 2:
    print("Quantidade inválida")
else:
    for i in range(1, qtd_linhas + 1):
        print("*" * i)