# 19. Pesquise e explique a diferenca entre copia rasa e copia profunda em Python. Crie um exemplo usando copy.copy() e copy.deepcopy().
# Cópia rasa copia apenas a estrutura principal. Cópia profunda copia também os objetos internos.

import copy

lista = [[1, 2], [3, 4]]

copia_rasa = copy.copy(lista)
copia_profunda = copy.deepcopy(lista)

copia_rasa[0][0] = 99
print(lista)

copia_profunda[1][0] = 88
print(lista)
print(copia_profunda)