# 17. Use o metodo copy() para criar uma copia de uma lista. Altere a copia e mostre que a lista original nao foi modificada.

lista = [1, 2, 3]
copia = lista.copy()

copia[0] = 10

print(lista)
print(copia)