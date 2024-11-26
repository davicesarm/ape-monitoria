#Os prints nao estao no padrao pedido, resoluçao apenas para ensino

carrinho = 0
boneca = 0
n = int(input())

for i in range(n):
    nome, sexo = input().split()
    if sexo == "m":
        carrinho += 1
    else:
        boneca += 1

print(carrinho)
print(boneca)