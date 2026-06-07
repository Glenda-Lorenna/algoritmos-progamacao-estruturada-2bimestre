# 11. Crie um programa que compare duas variaveis usando == e is, mostrando a diferenca entre comparar valores e comparar referencias.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(lista1 == lista2)
print(lista1 is lista2)
print(lista1 is lista3)