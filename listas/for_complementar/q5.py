""" Faça um programa que gere a tabuada 
de 1 a 10. Mostre a tabuada na forma: 
1x1 = 1
1x2 = 2
"""

for i in range(1, 11):
    for j in range(1, 11): 
        print(f"{i} x {j} = {i * j}")
    print()