# 13. Exiba o filho esquerdo e o filho direito da raiz de uma arvore binaria.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(10)
raiz.esquerda = No(5)
raiz.direita = No(20)

print("Filho esquerdo:", raiz.esquerda.valor)
print("Filho direito:", raiz.direita.valor)
