# 17. Pesquise e explique o percurso em pos-ordem. Pós-ordem visita primeiro a esquerda, depois a direita e por último a raiz.

def pos_ordem(no):
    if no:
        pos_ordem(no.esquerda)
        pos_ordem(no.direita)
        print(no.valor)