"""
enumerate = enumera iteráveis (índices)
"""

lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')

# lista_enumerada = list(enumerate(lista))

for item in enumerate(lista):
    print(item)

for key, value in enumerate(lista, start=1000):
    print(key, value)

for item in enumerate(lista):
    indice, nome = item
    print(indice, nome, lista[indice])


for tupla_enumerada in enumerate(lista):
    print('FOR da tupla:')
    for valor in tupla_enumerada:
        print(f'\t{valor}')
