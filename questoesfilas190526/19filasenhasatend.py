# 19. Crie um programa que simule uma fila de senhas de atendimento, exibindo a senha chamada a cada atendimento.

def enfileirar(fila, valor):
    fila.append(valor)
def desenfileirar(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return None

fila_senhas = []
senha_atual = 1

while True:
    print("\n1 - Gerar senha")
    print("2 - Chamar próxima senha")
    print("3 - Sair")

    op = input("Escolha: ")

    if op == "1":
        senha = f"S{senha_atual}"
        enfileirar(fila_senhas, senha)
        print(f"Senha gerada: {senha}")
        senha_atual += 1

    elif op == "2":
        senha = desenfileirar(fila_senhas)
        if senha:
            print(f"Chamando: {senha}")
        else:
            print("Nenhuma senha na fila")

    elif op == "3":
        break
    else:        
        print("Opção inválida")

