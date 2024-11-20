""" Faça um programa que leia um número 
inteiro N, calcule e mostre o maior
quadrado perfeito menor ou igual a N.
Por exemplo, se N for igual a 38, o resultado é 36 """

n = int(input())
for i in range(n - 1, -1,-1):
    if i * i <= n:
        print(i * i)
        break