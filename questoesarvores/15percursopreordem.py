# 15. Pesquise e explique o percurso em pre-ordem. Pré-ordem visita primeiro a raiz, depois a esquerda e depois a direita.

def pre_ordem(no):
    if no:
        print(no.valor)
        pre_ordem(no.esquerda)
        pre_ordem(no.direita)