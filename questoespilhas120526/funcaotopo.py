# 14. Crie uma funcao chamada topo(pilha) que retorne o ultimo elemento da pilha sem remove-lo.

def topo(pilha):
    if len(pilha) == 0:
        return None  # Retorna None se a pilha estiver vazia
    return pilha[-1]  # Retorna o ultimo elemento da pilha sem remove-lo  