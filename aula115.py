# considerando duas listas de inteiros ou floats
# some os valores nas listas retornando uma nova lista com os valores somados

# se uma lista for maior que a outra, a soma só vai considerar o tamanho menor

# lista_a = [1, 2, 3, 4, 5, 6, 7]
# lista_b = [1, 2, 3, 4]

# resultado
# lista_soma = [2, 4, 6, 8]

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
lista_soma3 = [
    x + y for x, y in zip(lista_a, lista_b)
]

lista_soma1 = []
for i in range(len(lista_b)):
    lista_soma1.append(lista_a[i] + lista_b[i])
print(lista_soma1)

lista_soma2 = []
for i, _ in enumerate(lista_b):
    lista_soma2.append(lista_a[i] + lista_b[i])
print(lista_soma2)

print(lista_soma3)
