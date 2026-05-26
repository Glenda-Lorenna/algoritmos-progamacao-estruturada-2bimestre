# Depois de armazenar cinco nomes em uma pilha, remova e exiba os nomes na ordem inversa em que foram digitados. 

pilha = []

for i in range(5):
    nome = input("Digite um nome: ")
    pilha.append(nome)
print("Nomes na pilha:", pilha)
print("Removendo e exibindo os nomes na ordem inversa:")

while pilha:
    nome_removido = pilha.pop()
    print(nome_removido)
    print("Pilha após remoção de todos os nomes:", pilha)