import math

x = float(input("Digite o valor de x (em radianos): "))


termos = 20

# Reduz x ao intervalo [0, 2*pi] para maior precisão
x = x % (2 * math.pi)
cosseno = 0

for n in range(termos):
    fatorial = 1
    for i in range(1, 2 * n + 1):
        fatorial *= i
    termo = ((-1) ** n) * (x ** (2 * n)) / fatorial
    cosseno += termo

resultado = cosseno
resultado_math = math.cos(x)

print(f"O valor do cosseno de {x} usando a série é aproximadamente {resultado}")
print(f"O valor do cosseno de {x} usando math.cos é {resultado_math}")

