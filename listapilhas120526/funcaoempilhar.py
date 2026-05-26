# Crie uma funcao chamada empilhar(pilha, valor) que adicione um valor na pilha. 

def empilhar(pilha, valor):
    pilha.append(valor)

# Exemplo de uso
pilha = []
empilhar(pilha, 10)
empilhar(pilha, 20)
empilhar(pilha, 30)
print("Pilha após empilhar valores:", pilha)