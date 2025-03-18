# Questao 1

def qtd_ocorrencias(matriz: list, valor) -> int:
    qtd = 0
    for i in matriz:
        for j in i:
            if j == valor:
                qtd += 1
    return qtd

# ------------------

# Questao 2
def criptografar(texto: str) -> str:
    texto = texto.replace("a", "@")
    texto = texto.replace("A", "@")
    texto = texto.replace("e", "3")
    texto = texto.replace("E", "3")
    texto = texto.replace("i", "1")
    texto = texto.replace("I", "1")
    return texto


def criptografar2(texto: str) -> str:
    nova_string = ""
    for letra in texto:
        if letra.lower() == "a":
            nova_string += "@"
        elif letra.lower() == "e":
            nova_string += "3"
        elif letra.lower() == "i":
            nova_string += "1"
        else:
            nova_string += letra
    return nova_string

frase = input()
print(criptografar2(frase))
print(criptografar(frase))
    
# ------------------
        
# Questao 3

def gerar_identificador(data: str, nome: str) -> str:
    dia, mes, ano = data.split("/")
    nova_data = ano + mes + dia
    nome_lista = nome.split()
    primeiro_nome = nome_lista[0].capitalize()
    ultimo_nome = nome_lista[-1].capitalize()
    nome = primeiro_nome + ultimo_nome
    
    identificador = nova_data
    return identificador + "_" + nome

data = input()
nome_completo = input()
identificador = gerar_identificador(data, nome_completo)
print(identificador)

