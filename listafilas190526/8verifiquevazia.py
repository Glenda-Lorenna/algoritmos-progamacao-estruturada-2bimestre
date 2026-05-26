# Faça um programa que verifique se uma fila está vazia antes de remover um elemento.

fila = []
if not fila:
    print("A fila está vazia. Não é possível remover elementos.")
else:
    removido = fila.pop(0)
    print("Valor removido:", removido)
    print("Fila após remoção:", fila)
    