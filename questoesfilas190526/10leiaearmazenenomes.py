# Faca um programa que leia cinco nomes digitados pelo usuario e armazene todos em uma fila.

fila = []

for i in range(5):
    nome = input("Digite um nome: ")
    fila.append(nome)

print("Fila:", fila)