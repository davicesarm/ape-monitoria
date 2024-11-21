# 01) Escreva um programa que exiba 20 vezes a mensagem “Estou aprendendo o comando for”.

for i in range(20):
    print("Estou aprendendo o comando for")

# 03) Faça um programa que leia 3 números inteiros (N, X, Y) e mostre todos os números múltiplos de N entre X e Y.

valor = int(input("Digite o valor: "))
x = int(input("Digite o inicio do intervalo: "))
y = int(input("Digite o fim do intervalo: "))

for i in range(x, y): #(1,11) - 1 ate o 10
    if i % valor == 0:
        print(i)

# 7 14 21 28 35 42 49



