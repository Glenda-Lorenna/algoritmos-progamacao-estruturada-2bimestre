# Crie um programa que remova todos os elementos de uma pilha, um por vez, mostrando cada elemento removido. 

pilha = [10, 20, 30, 40, 50]
while pilha:
    valor_removido = pilha.pop()
    print("Valor removido:", valor_removido)
print("Pilha após remoção de todos os elementos:", pilha)