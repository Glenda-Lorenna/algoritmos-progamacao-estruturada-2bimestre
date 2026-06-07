# 5. Altere o valor da variavel numero depois de criar referencia. O valor de referencia tambem muda? Explique o resultado em Python.

numero = 10
referencia = numero

numero = 20

print(numero)
print(referencia)

# Resposta: Isso acontece porque inteiros são imutáveis em Python. Ao mudar numero, ele passa a apontar para outro objeto.