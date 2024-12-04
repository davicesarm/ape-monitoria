# Questao 4

qtd_falsas = 0
soma_precos = 0

while True:
    valor_antes = float(input()) # 90
    valor_durante = float(input()) # 100

    desconto = valor_antes - valor_durante
    
    if desconto > 0:
        break

    qtd_falsas += 1
    soma_precos += valor_durante

 
media = soma_precos / qtd_falsas
print(qtd_falsas)
print(media)