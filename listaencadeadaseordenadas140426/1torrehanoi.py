# Torre de Hanói - solução recursiva
# A ideia é mover discos de uma torre para outra seguindo regras:
# 1. Só pode mover um disco por vez
# 2. Um disco maior nunca pode ficar em cima de um menor

def hanoi(n, origem, destino, auxiliar):
    # Caso base: se houver apenas 1 disco
    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    
    # Passo 1: mover n-1 discos da origem para a torre auxiliar
    # usando a torre destino como apoio
    hanoi(n - 1, origem, auxiliar, destino)
    
    # Passo 2: mover o maior disco (o último) para o destino
    print(f"Mover disco {n} de {origem} para {destino}")
    
    # Passo 3: mover os n-1 discos da torre auxiliar para o destino
    # usando a torre origem como apoio
    hanoi(n - 1, auxiliar, destino, origem)


# Teste
print("Resolução da Torre de Hanói com 3 discos:\n")
hanoi(3, 'A', 'C', 'B')