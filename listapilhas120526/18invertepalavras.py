# 18. Use uma pilha para inverter uma palavra digitada pelo usuario.

def inverter_palavra(palavra):
    pilha = []  # Cria uma pilha vazia
    for letra in palavra:
        pilha.append(letra)  # Empilha cada letra da palavra

    palavra_invertida = ''
    while pilha:
        palavra_invertida += pilha.pop()  # Desempilha as letras e forma a palavra invertida

    return palavra_invertida    