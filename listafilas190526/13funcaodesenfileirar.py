# Crie uma funcao chamada desenfileirar(fila) que remova e retorne o primeiro elemento da fila.

def desenfileirar(fila):
    if len(fila) == 0:
        return None  # Retorna None se a fila estiver vazia
    return fila.pop(0)  # Remove e retorna o primeiro elemento da fila