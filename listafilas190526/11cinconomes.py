# Depois de armazenar cinco nomes em uma fila, remova e exiba os nomes na mesma ordem em que foram digitados.

fila = []

for i in range(5):
    nome = input("Digite um nome: ")
    fila.append(nome)
print("Fila:", fila)
print("Removendo nomes da fila:")

while len(fila) > 0:
    nome_removido = fila.pop(0)
    print("Nome removido:", nome_removido)