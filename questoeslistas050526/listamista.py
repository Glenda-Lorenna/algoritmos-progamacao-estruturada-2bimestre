# Crie uma lista com diferentes tipos de dados:
dados = []

# Inserindo dados
nome = input("Digite um nome: ")
idade = int(input("Digite uma idade: "))
altura = float(input("Digite uma altura: "))
aprovado = bool(input("O aluno foi aprovado? (True/False): "))

# Convertendo para booleano
aprovado = aprovado == "True" 

# Adicionando os dados à lista
dados.append(nome)
dados.append(idade)
dados.append(altura)
dados.append(aprovado)

# Exibindo o dados separadamente
print("Nome:", dados[0])
print("Idade:", dados[1])
print("Altura:", dados[2])
print("Aprovado:", dados[3])