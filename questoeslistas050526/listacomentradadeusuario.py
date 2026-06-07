# Criando uma lista de entrada do usuário
numeros = []

# Solicitando ao usuário que insira 5 números
for i in range(5):
    numero = int(input(f"Digite um número: "))
    numeros.append(numero)

# Mostrando a lista de números inseridos pelo usuário
print("Números inseridos:", numeros)

# Somando valores da lista
soma = sum(numeros)
print("Soma dos números:", soma)