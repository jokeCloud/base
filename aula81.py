# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

import copy

d1 = {
    'c1': 1,
    'c2': 2,
}

d2 = d1

print(d2, d1)


d2['c1'] = 100

print(d2, d1)


d2 = d1.copy()

d2['c1'] = 1000

print(d2, d1)


d3 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d4 = d3.copy()

d4['c1'] = 10000
d4['l1'][1] = 20000

print(d3)
print(d4)


d4 = copy.deepcopy(d3)

d4['c1'] = 10000
d4['l1'][1] = 20000

print(d3)
print(d4)
