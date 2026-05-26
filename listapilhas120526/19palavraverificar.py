# 19. Crie um programa que use uma pilha para verificar se uma palavra e um palindromo.

def verificar_palindromo(palavra):
    pilha = []  # Cria uma pilha vazia
    for letra in palavra:
        pilha.append(letra)  # Empilha cada letra da palavra

    palavra_invertida = ''
    while pilha:
        palavra_invertida += pilha.pop()  # Desempilha as letras e forma a palavra invertida

    return palavra == palavra_invertida  # Verifica se a palavra é igual à sua versão invertida