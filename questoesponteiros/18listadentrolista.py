# 18. Crie uma lista dentro de outra lista e faca uma copia com copy(). Altere a lista interna e observe o que acontece com a lista original.

lista = [[1, 2], [3, 4]]
copia = lista.copy()

copia[0][0] = 99

print(lista)
print(copia)

# A lista original também é alterada na parte interna, porque copy() faz cópia rasa.