# funcao lambda
# funcoes anonimas que contem apenas uma linha
lista = [
    {'nome': 'joão', 'sobrenome': 'michael'},
    {'nome': 'maria', 'sobrenome': 'gabriel'},
    {'nome': 'jose', 'sobrenome': 'rafael'},
    {'nome': 'madalena', 'sobrenome': 'teresa'},
    {'nome': 'pedro', 'sobrenome': 'paulo'},
]


# def ordena(item):
#     return item['nome']


# lista.sort(key=ordena)

# lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)


for item in lista:
    print(item)
