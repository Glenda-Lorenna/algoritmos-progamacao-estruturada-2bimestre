# Crie uma pilha com nomes de livros e mostre qual livro esta no topo da pilha. 

pilha = ["O Senhor dos Anéis", "Crime e Castigo", "Noites Brancas", "Orguljo e Preconceito", "Dom Casmurro"]
if pilha:
    livro_topo = pilha[-1]
    print("Livro no topo da pilha:", livro_topo)
else:
    print("A pilha está vazia. Não há livros para mostrar.")