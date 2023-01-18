import copy

from dados import produtos

# aumente os preços dos produtos em 10%
# gere novos_produtos por deep copy (copia profunda)

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# ordene os produtos por nome decrescente
# gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome']
)


# ordene os produtos por preco crescente
# gere produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['preco']
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
