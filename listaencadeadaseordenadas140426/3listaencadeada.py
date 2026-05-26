# 3 - Em Python, desenvolva uma lista ordenadas para receber 57 nomes de alunos

def extrair_numero(nome):
    # Pega o número depois do "_"
    return int(nome.split("_")[1])


class Node:
    def __init__(self, nome):
        self.nome = nome
        self.next = None


class ListaOrdenada:
    def __init__(self):
        self.head = None

    def inserir_ordenado(self, nome):
        novo = Node(nome)

        # Extrai número do novo nome
        num_novo = extrair_numero(nome)

        # Inserir no início
        if self.head is None or num_novo < extrair_numero(self.head.nome):
            novo.next = self.head
            self.head = novo
            return

        atual = self.head

        # Percorre (tipo i++)
        while atual.next and extrair_numero(atual.next.nome) < num_novo:
            atual = atual.next

        novo.next = atual.next
        atual.next = novo

    def imprimir(self):
        atual = self.head
        i = 0

        while atual:
            print(f"{i} - {atual.nome}")
            atual = atual.next
            i += 1

if __name__ == "__main__":
    lista_alunos = ListaOrdenada()

    # Inserindo 57 nomes
    for i in range(57):
        nome = f"Aluno_{57 - i}"  # fora de ordem de propósito
        lista_alunos.inserir_ordenado(nome)

    print("Lista ordenada de alunos:\n")
    lista_alunos.imprimir()            