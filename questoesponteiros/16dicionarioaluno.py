# 16. Crie um dicionario chamado aluno com nome e idade. Crie uma segunda variavel chamada referencia_aluno apontando para o mesmo dicionario. Altere a idade usando referencia_aluno e exiba aluno.

aluno = {"nome": "Ana", "idade": 18}
referencia_aluno = aluno

referencia_aluno["idade"] = 19

print(aluno)