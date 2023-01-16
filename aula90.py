# list comprehension
# forma rapida de criar listas a partir de iteraveis
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)
print(lista)

lista = [numero for numero in range(10)]
print(lista)

lista = [numero * 2 for numero in range(10)]
print(lista)

lista = [
    numero * 3
    for numero in range(10)
]
print(lista)
