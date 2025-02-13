# m = [[1,2,3],
#      [2,3,4],
#      [4,5,6]]

import random

LINHAS = 10
COLUNAS = 15

m = [[0] * COLUNAS] * LINHAS # NAO FUNCIONA CUIDADO!!!!!!!!

m = [0] * LINHAS

for i in range(LINHAS):
    linha = [0] * COLUNAS
    for j in range(COLUNAS):
        linha[j] = random.randint(1, 20)
    m[i] = linha

m = [
    [0] * COLUNAS 
    for _ in range(LINHAS)
]

for i in range(LINHAS):
    for j in range(COLUNAS):
        m[i][j] = random.randint(1, 20)

print(*m, sep="\n")