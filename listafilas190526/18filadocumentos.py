# 18. Use uma fila para organizar a ordem de impressao de documentos digitados pelo usuario.

fila_impressao = []

while True:
    print("\n1 - Adicionar documento")
    print("2 - Imprimir documento")
    print("3 - Sair")

    op = input("Escolha: ")

    if op == "1":
        doc = input("Nome do documento: ")
        fila_impressao.append(doc)

    elif op == "2":
        if fila_impressao:
            doc = fila_impressao.pop(0)
            print(f"Imprimindo: {doc}")
        else:
            print("Nenhum documento na fila")

    elif op == "3":
        break

