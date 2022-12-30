"""
for in com listas
"""

lista = ['Maria', 'João', 'José']
lista_numeros = [1, 2, 3]
lista.append('Paulo')

indices = range(len(lista))


for letra in 'ABC':
    print(letra, type(letra))

for item in lista:
    print(item)

for _ in lista_numeros:
    print(_)

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))
