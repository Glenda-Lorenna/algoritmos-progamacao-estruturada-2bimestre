# 20. Crie um programa em Python que simule ponteiros usando referencias: duas variaveis devem apontar para a mesma lista, uma deve modificar a lista e a outra deve mostrar a alteracao.

lista1 = [1, 2, 3]
lista2 = lista1

lista1.append(4)

print(lista2)