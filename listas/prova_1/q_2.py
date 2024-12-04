# Questao 2

valor_antes = float(input())
valor_durante = float(input())

desconto = ((valor_antes - valor_durante) / valor_antes) * 100

if (valor_durante > valor_antes) or (valor_durante == valor_antes):
    print("Desonesto")
elif desconto <= 20:
    print("Honesto")
elif desconto <= 50:
    print("Muito honesto")
else:
    print("Aburdamente honesto")