# 19. Faca um programa que calcule a altura de uma arvore binaria.

def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no.esquerda), altura(no.direita))