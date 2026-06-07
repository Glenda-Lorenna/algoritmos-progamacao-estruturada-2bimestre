# 16. Pesquise e explique o percurso em ordem. Em ordem visita primeiro a esquerda, depois a raiz e depois a direita.

def em_ordem(no):
    if no:
        em_ordem(no.esquerda)
        print(no.valor)
        em_ordem(no.direita)