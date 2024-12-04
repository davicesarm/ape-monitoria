""" Q3 - Serão lidos indeterminados números positivos ou negativos, o programa deve parar quando o número digitado for 0. Ao final do programa, deve ser impresso a soma total de todos os números pares, a soma total de todos os números impares e qual foi o maior par e qual foi o maior impar. """
soma_pares = 0
soma_impares = 0
maior_par = 1
maior_impar = 0

while True:
    num = int(input())
    
    if num == 0:
        break

    if num % 2 == 0:
        soma_pares += num
        if (maior_par == 1) or (num > maior_par):
            maior_par = num
    
    elif num % 2 != 0:
        soma_impares += num
        if (maior_impar == 0) or (num > maior_impar):
            maior_impar = num
            

print(soma_pares)
print(soma_impares)

if maior_impar == 0:
    print("Não houve impares")
else:
    print(maior_impar)
    
if maior_par == 1:
    print("Não houve pares")
else:
    print(maior_par)