# 12. Crie uma funcao chamada alterar_lista(lista) que receba uma lista e adicione um novo elemento nela. Depois, mostre que a lista original foi modificada.

def alterar_lista(lista):
    lista.append(4)

valores = [1, 2, 3]
alterar_lista(valores)

print(valores)