# 20. Pesquise uma situacao do mundo real em que o conceito de fila pode ser aplicado e escreva um exemplo em Python.
# Exemplo: Fila de atendimento em um banco

class FilaBanco:
    def __init__(self):
        self.fila = []  # Cria uma fila vazia

    def entrar_fila(self, cliente):
        self.fila.append(cliente)  # Adiciona um cliente ao final da fila
        print(f"{cliente} entrou na fila.")

    def atender_cliente(self):
        if self.fila:
            cliente_atendido = self.fila.pop(0)  # Remove o cliente do início da fila
            print(f"{cliente_atendido} foi atendido.")
        else:
            print("A fila está vazia. Nenhum cliente para atender.")