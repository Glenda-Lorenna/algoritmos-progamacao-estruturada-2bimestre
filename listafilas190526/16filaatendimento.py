# 16. Faca um programa que simule uma fila de atendimento. O usuario deve poder adicionar pessoas e atender a primeira pessoa da fila.

fila = []

while True:
    print("\n1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        fila.append(nome)

    elif opcao == "2":
        if fila:
            pessoa = fila.pop(0)
            print(f"Atendendo: {pessoa}")
        else:
            print("Fila vazia")

    elif opcao == "3":
        break
    else:
            print("Fila vazia")
    
