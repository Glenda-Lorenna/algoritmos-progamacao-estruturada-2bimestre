# 13. Crie uma funcao chamada desempilhar(pilha) que remova e retorne o elemento do topo da pilha.

def desempilhar(pilha):
    if len(pilha) == 0:
        return None  # Retorna None se a pilha estiver vazia
    return pilha.pop()  # Remove e retorna o elemento do topo da pilha