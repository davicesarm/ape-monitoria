#Não segue o exercicio, apenas uma maneira de fazer
alcool = 0
gasolina = 0
diesel = 0

print("1.Comprar Alcool")
print("2.Comprar Gasolina")
print("3.Comprar Diesel")
print("4.Fim")

while True:
    
    opcao = int(input("Qual combustivel: "))

    # se o usuario digitar outro numero so deve ser perguntado outro

    if opcao == 1:
        alcool = alcool + 1
    elif opcao == 2:
        gasolina = gasolina + 1
    elif opcao == 3:
        diesel += 1
    elif opcao == 4:
        break # para instantaneamente
    else:
        continue # volte para inicio do loop
        
    print("Voce digitou um numero correto")

  
print("MUITO OBRIGADO")
print(f"Gasolina:{gasolina}")
print(f"Alcool:{alcool}")
print(f"Diesel:{diesel}")