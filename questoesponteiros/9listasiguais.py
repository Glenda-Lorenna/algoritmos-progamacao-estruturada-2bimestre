# 9. Crie duas listas iguais usando valores diferentes, por exemplo lista1 = [1, 2, 3] e lista2 = [1, 2, 3]. Use id() para verificar se elas sao o mesmo objeto.

lista1 = [1, 2, 3]
lista2 = [1, 2, 3]

print(id(lista1))
print(id(lista2))

# Os valores são iguais, mas os identificadores geralmente são diferentes.