# Crie uma funcao chamada primeiro(fila) que retorne o primeiro elemento da fila sem remove-lo.

def primeiro(fila):
    if len(fila) == 0:
        return None  # Retorna None se a fila estiver vazia
    return fila[0]  # Retorna o primeiro elemento da fila sem removê-lo
