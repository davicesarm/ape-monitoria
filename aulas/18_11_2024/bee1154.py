soma_das_idades = 0
qtd_idades = 0

while True:
    idade = int(input())
    
    if idade < 0:
        break
    
    soma_das_idades += idade
    qtd_idades += 1
    
media = soma_das_idades / qtd_idades
print(f"{media:.2f}")