# 18. Faca um programa que conte quantos nos existem em uma arvore binaria.

def contar_nos(no):
    if no is None:
        return 0
    return 1 + contar_nos(no.esquerda) + contar_nos(no.direita)