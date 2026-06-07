# Crie uma lista com números de 1 a 20 e exiba apenas os números pares.

numeros = list(range(1, 21))

# Filtrando os números pares
pares = [num for num in numeros if num % 2 == 0]

# Exibindo os números pares
print("Números pares de 1 a 20:", pares)