# 17. Crie um menu com as opcoes: enfileirar, desenfileirar, mostrar primeiro, mostrar fila e sair.

def enfileirar(fila, valor):
    fila.append(valor)
def desenfileirar(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return "Fila vazia"
def primeiro(fila):
    if len(fila) > 0:
        return fila[0]
    else:
        return "Fila vazia"
    
fila = []

while True:
    print("\n1 - Enfileirar")
    print("2 - Desenfileirar")
    print("3 - Mostrar primeiro")
    print("4 - Mostrar fila")
    print("5 - Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        valor = input("Digite um valor: ")
        enfileirar(fila, valor)

    elif opcao == "2":
        print("Removido:", desenfileirar(fila))

    elif opcao == "3":
        print("Primeiro:", primeiro(fila))

    elif opcao == "4":
        print("Fila:", fila)

    elif opcao == "5":
        break