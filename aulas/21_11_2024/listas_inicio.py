chamada = [1,2,3,4,5,6,7,8,9,10]
pessoas = ["joao", "maria", "pedro", "jose", "ana", "maria", "pedro", "jose", "ana", "maria",["davi leite","davi cesar"]]
lista_vazia = []

while True:
    print("1. Adicionar uma pessoa")
    print("2. Printar a lista")
    print("3. Sair")
    entrada = input()

    if entrada == '1':
        pessoa = input("Digite o nome da pessoa: ")
        lista_vazia.append(pessoa)
    
    elif entrada == '2':
        print(lista_vazia)
    
    elif entrada == '3':
        break

print(lista_vazia)