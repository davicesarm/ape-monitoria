""" Escreva um algoritmo que lê um valor 
n inteiro e positivo e que calcula a seguinte soma """

n = int(input())

s = 1

for i in range(2, n + 1):
    s += (1 / i)
    
print(s)