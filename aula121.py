# reduce - faz a reducao de um iteravel em um valor
# traz um resultado de um iteravel, como somar todos
from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 20},
    {'nome': 'Produto 3', 'preco': 30},
    {'nome': 'Produto 2', 'preco': 40},
    {'nome': 'Produto 4', 'preco': 50},
]

total = 0
for p in produtos:
    total += p['preco']


def funcao_de_reduce(acumulador, produto):
    print('acumulador:', acumulador)
    print('produto:', produto)
    print()
    return acumulador + produto['preco']


totall = reduce(
    # funcao_de_reduce,
    lambda ac, p: ac + p['preco'],
    produtos,
    0.0,
)

print('total é:', total)

print(round(sum([p['preco'] for p in produtos]), 2))
