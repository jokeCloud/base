# combinations, permutations e product - itertools
# combinação - ordem não importa - iterável + tamanho do grupo
# permutação - ordem importa
# produto - ordem importa e repete valores únicos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'joão', 'joana', 'luiz', 'leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

# print(f'grupo de 2: {list(combinations(pessoas, 2))}')
# print(f'grupo de 3: {list(combinations(pessoas, 3))}')
# print(f'grupo de 2: {list(permutations(pessoas, 2))}')
# print(f'grupo de 3: {list(permutations(pessoas, 3))}')


# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))
