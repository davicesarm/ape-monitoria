# Frase com algumas palavras repetidas
frase = "Python é uma linguagem de programação versátil e poderosa. Com Python, é possível desenvolver desde scripts simples até aplicações complexas. Python é conhecido por sua sintaxe clara e intuitiva, facilitando o aprendizado."

palavras = ["davi", "python", "palavra"]
frequencias = [2, 2, 1]

for palavra in frase.split():
    palavra = palavra.strip(",.")
    
    if palavra not in palavras:
        palavras.append(palavra)
        frequencias.append(1)
    else:
        indice = palavras.index(palavra)
        frequencias[indice] += 1


palavras_frequentes = []
maior = max(frequencias)
for i in range(len(palavras)):
    if frequencias[i] == maior:
        palavras_frequentes.append(palavras[i])



# palavras_frequentes = [palavras[x] for x in range(len(palavras)) if frequencias[x] == max(frequencias)]

frase_lista = frase.split()

indices_palavras_frequentes = []
for i in range(len(frase_lista)):
    if frase_lista[i].strip(",.") in palavras_frequentes:
        indices_palavras_frequentes.append(i)
        
for i in indices_palavras_frequentes:
    print(i, frase_lista[i].strip(",."))
    
