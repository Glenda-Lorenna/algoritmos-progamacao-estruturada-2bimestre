# 17. Crie um menu com as opcoes: empilhar, desempilhar, mostrar topo, mostrar pilha e sair.

def menu():
    pilha = []  # Cria uma pilha vazia
    while True:
        print("Menu:")
        print("1. Empilhar")
        print("2. Desempilhar")
        print("3. Mostrar topo")
        print("4. Mostrar pilha")
        print("5. Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == '1':
            item = input("Digite o item para empilhar: ")
            pilha.append(item)  # Empilha o item
            print(f"{item} empilhado com sucesso.")
        elif opcao == '2':
            if pilha:
                item = pilha.pop()  # Desempilha o item do topo
                print(f"{item} desempilhado com sucesso.")
            else:
                print("A pilha esta vazia.")
        elif opcao == '3':
            if pilha:
                print(f"Topo da pilha: {pilha[-1]}")  # Mostra o item do topo
            else:
                print("A pilha esta vazia.")
        elif opcao == '4':
            if pilha:
                print("Pilha:", pilha)  # Mostra todos os itens da pilha
            else:
                print("A pilha esta vazia.")
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opcao invalida. Tente novamente.")