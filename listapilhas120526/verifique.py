# Faca um programa que verifique se uma pilha esta vazia antes de remover um elemento.

pilha = [10, 20, 30, 40, 50]
if pilha:
    valor_removido = pilha.pop()
    print("Valor removido:", valor_removido)
else:    
    print("A pilha está vazia. Não é possível remover elementos.")
    