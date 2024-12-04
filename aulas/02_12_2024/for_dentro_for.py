# Tabuada

# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

for _ in range(5):
    n = int(input())

    resultado_fatorial = 1
    for i in range(2, n + 1):
        resultado_fatorial = resultado_fatorial * i

    print(resultado_fatorial)
    
  
# LE UM NUMERO
# CALCULA O FATORIAL
# PRINTA O RESULTADO
# REPETE (quantas vezes? 5)
