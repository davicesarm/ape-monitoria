# Questao 3

qtd_promocoes_vdd = 0
maior_desconto = -1

for _ in range(2):
    valor_antes = float(input())
    valor_durante = float(input())
    
    desconto = valor_antes - valor_durante
    
    if desconto > 0:
        qtd_promocoes_vdd += 1
        
    if desconto > maior_desconto:
        maior_desconto = desconto

if qtd_promocoes_vdd == 0:
    print("Não houve promocoes de verdade")
else:
    print(qtd_promocoes_vdd)
    print(maior_desconto)