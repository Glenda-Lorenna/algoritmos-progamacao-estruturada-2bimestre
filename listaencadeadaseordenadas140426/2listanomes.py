# 2 - Em python, desenvolva uma lista encadeada para receber 50 nomes
# Estrutura do nó (cada elemento da lista)
class Node:
    def __init__(self, nome):
        self.nome = nome      # guarda o nome
        self.next = None      # aponta para o próximo nó


class ListaEncadeada:
    def __init__(self):
        self.head = None  # início da lista

    def inserir(self, nome):
        # Cria um novo nó
        novo = Node(nome)

        # Se a lista estiver vazia, o novo nó vira o início
        if self.head is None:
            self.head = novo
        else:
            # Percorre até o final da lista (simulando um i++)
            atual = self.head
            while atual.next:
                atual = atual.next  # avanço (como i++)
            
            # Liga o último nó ao novo
            atual.next = novo

    def imprimir(self):
        atual = self.head
        i = 0  # contador (equivalente ao i++)

        while atual:
            print(f"{i} - {atual.nome}")
            atual = atual.next
            i += 1


# Criando a lista
lista = ListaEncadeada()

# Inserindo 50 nomes (exemplo automático)
for i in range(50):
    nome = f"Nome_{i+1}"
    lista.inserir(nome)

print("Lista com 50 nomes:\n")
lista.imprimir()