'''
    Nome: lib_vogais
    Descrição: Biblioteca para manipulação de vogais em textos.
    Autores: Valéria Cavalcanti, <seu_nome>
    Data: 27/02/2025
    Versão: 1.0
'''
import random

# Verifica se um determinado símbolo é vogal.
def eh_vogal(simbolo: str) -> bool:
    return simbolo.lower() in "aeiou"

# Verifica se um texto é formado apenas por vogais.
def eh_texto_vogal(texto: str) -> bool:
    for letra in texto:
        if not eh_vogal(letra):
            return False
    return True

# Retorna a quantidade de vogais em um texto.
def quantidade_vogais(texto: str) -> int:
    qtd = 0
    for letra in texto:
        if eh_vogal(letra):
            qtd += 1
    return qtd

# Remove as vogais de um texto.
def remove_vogais(texto:str) -> str:
    novo_texto = ""
    for letra in texto:
        if not eh_vogal(letra):
            novo_texto += letra

# Identifica as vogais que estão presentes em um texto.
def identifica_vogais(texto: str) -> list:
    vogais = []
    for letra in texto:
        if eh_vogal(letra) and letra not in vogais:
            vogais.append(letra)
    return vogais

# Frequêcia de vogais em um texto.
def frequencia_vogais(texto: str) -> list:
    vogais = "aeiou"
    frequencias = [0] * 5
    for letra in texto:
        if eh_vogal(letra):
            frequencias[vogais.index(letra.lower())] += 1
            
    return frequencias
        

# Substitui as vogais de um texto por * (asterísco).
def substitui_vogais(texto: str) -> str:
    novo_texto = ""
    for letra in texto:
        if eh_vogal(letra):
            novo_texto += "*"
        else:
            novo_texto += letra

# Identifica a vogal que mais aparece em um texto. Pode haver mais de uma vogal com a mesma frequência.
def vogal_mais_frequente(texto: str) -> list:
    frequencias = frequencia_vogais(texto)
    vogais = "aeiou"
    vogais_frequentes = []
    for i in range(len(frequencias)):
        if frequencias[i] == max(frequencias):
            vogais_frequentes.append(vogais[i])
            
    return vogais_frequentes

# Sortear uma vogal.
def sortear_vogal() -> str:
    return random.choice("aeiou")

    