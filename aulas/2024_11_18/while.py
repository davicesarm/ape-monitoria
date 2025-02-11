# Diferença entre for e while

# while é baseado em uma condiçao (assim como o if)

# for passa por todos os elementos de uma sequencia (exemplo: range())

while (True):
    x = input()
    
    if x == '0':
        print("Entrou no 0")
        break
    
    print("Antes do continue")
    
    if x == '1':
        print("Entrou no 1")
        continue
    
    print("Depois do continue")

    
    
print("Fora do while")