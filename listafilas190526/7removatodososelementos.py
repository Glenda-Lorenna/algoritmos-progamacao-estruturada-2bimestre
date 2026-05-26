# Crie um programa que remova todos os elementos de uma fila, um por vez, mostrando cada elemento removido.

fila = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]
while fila:
    removido = fila.pop(0)
    print("Valor removido:", removido)
print("Fila após remoção de todos os elementos:", fila)

