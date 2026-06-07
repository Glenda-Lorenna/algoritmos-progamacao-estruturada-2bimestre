# Faca um programa que leia cinco nomes digitados pelo usuario e armazene todos em uma pilha.

pilha = []
for i in range(5):
    nome = input("Digite um nome: ")
    pilha.append(nome)

print("Nomes na pilha:", pilha)