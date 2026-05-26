# Cria uma lista com 5 frutas

frutas = ["maçã", "banana", "laranja", "uva", "abacaxi"]

print(f"Lista de frutas disponível: {frutas}")

fruta_remover = input("Qual fruta você deseja remover da lista? ").capitalize()

if fruta_remover in frutas:
    frutas.remove(fruta_remover)
    print(f"\nSucesso! '{fruta_remover}' foi removida.")
else:
    print(f"\nA fruta '{fruta_remover}' não foi encontrada na lista.")

print(f"Lista atualizada: {frutas}")