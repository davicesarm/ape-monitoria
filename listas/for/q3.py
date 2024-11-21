valor = int(input("Digite o valor: "))
x = int(input("Digite o inicio do intervalo: "))
y = int(input("Digite o fim do intervalo: "))

for i in range(x, y):
    if i % valor == 0:
        print(i)