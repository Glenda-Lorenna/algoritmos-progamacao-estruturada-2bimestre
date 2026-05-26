# 20. Pesquise uma situacao do mundo real em que o conceito de fila pode ser aplicado e escreva um exemplo em Python.
# Exemplo: Fila de atendimento em um shopping

def enfileirar(fila, cliente):
    fila.append(cliente)

def desenfileirar(fila):
    if len(fila) > 0:
        return fila.pop(0)
    else:
        return None

def esta_vazia(fila):
    return len(fila) == 0

fila_shopping = []

# Clientes chegando
enfileirar(fila_shopping, "Ana")
enfileirar(fila_shopping, "Bruno")
enfileirar(fila_shopping, "Carla")
enfileirar(fila_shopping, "Diego")

print("Fila atual:", fila_shopping)

# Atendimento no caixa
print("\nAtendimento iniciado...\n")

while not esta_vazia(fila_shopping):
    cliente = desenfileirar(fila_shopping)
    print(f"Atendendo cliente: {cliente}")

print("\nTodos os clientes foram atendidos.")
