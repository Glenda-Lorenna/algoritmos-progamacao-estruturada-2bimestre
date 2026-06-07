# 7. Crie uma arvore com um no raiz e dois filhos, depois exiba todos os valores.

arvore = {
    "valor": "Raiz",
    "filhos": ["Filho 1", "Filho 2"]
}

print(arvore["valor"])
for filho in arvore["filhos"]:
    print(filho)