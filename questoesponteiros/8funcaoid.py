# 8. Use a funcao id() para mostrar o identificador de memoria de duas variaveis que apontam para o mesmo objeto.

valores = [1, 2, 3]
ponteiro_lista = valores

print(id(valores))
print(id(ponteiro_lista))