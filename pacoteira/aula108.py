from copy import deepcopy

produtos = [
    {'nome': 'produto 5', 'preco': 50.00},
    {'nome': 'produto 1', 'preco': 10.00},
    {'nome': 'produto 3', 'preco': 30.00},
    {'nome': 'produto 2', 'preco': 20.00},
    {'nome': 'produto 4', 'preco': 40.00},
]

# aumente os preços dos produtos em 10%
# gere novos_produtos por deep copy (copia profunda)

novos_produtos = deepcopy(produtos)
novos_precos = [float(round(produto['preco'] * 1.10)) for produto in produtos]
# print(novos_produtos)
# print(novos_precos)

contador = 0
for produto in produtos:
    novos_produtos[contador]['preco'] = novos_precos[contador]
    contador += 1
for item in novos_produtos:
    print(item)


# ordene os produtos por nome decrescente
# gere produtos_ordenados_por_nome por deep copy
produtos_ordenados_por_nome = deepcopy(novos_produtos)
contador = 0
for chave, valor in produtos_ordenados_por_nome:
    print(set([chave[contador], valor[contador]]))

# ordene os produtos por preco crescente
# gere produtos_ordenados_por_preco por deep copy
produtos_ordenados_por_preco = deepcopy(novos_produtos)


# print(set([5, 4, 3, 2, 1]))
