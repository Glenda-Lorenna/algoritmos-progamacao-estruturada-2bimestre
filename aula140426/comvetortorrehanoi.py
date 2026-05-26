def torre_de_hanoi(n, origem, destino, auxiliar, movimentos):
    if n == 1:
        movimentos.append(f"Mover disco 1 de {origem} para {destino}")
        return
    
    torre_de_hanoi(n - 1, origem, auxiliar, destino, movimentos)
    
    movimentos.append(f"Mover disco {n} de {origem} para {destino}")
    
    torre_de_hanoi(n - 1, auxiliar, destino, origem, movimentos)


# Programa principal
n = int(input("Digite o número de discos: "))
movimentos = []  # vetor (lista)

torre_de_hanoi(n, 'A', 'C', 'B', movimentos)

# Exibindo os movimentos
for passo in movimentos:
    print(passo)