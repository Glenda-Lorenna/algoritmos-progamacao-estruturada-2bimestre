def contador(i, alunos):
    if i < 50:
        nome = input(f"Digite o nome do aluno {i + 1}: ")
        alunos.append(nome)
        contador(i + 1, alunos)  # chama a função novamente (recursão)
    else:
        print("\nLista de alunos:")
        for j in range(len(alunos)):
            print(f"{j + 1} - {alunos[j]}")

# lista vazia
alunos = []

# inicia o contador
contador(0, alunos)