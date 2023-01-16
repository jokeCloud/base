produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 40},
    {'nome': 'p3', 'preco': 60},
]

novos_produtos = [
    produto['nome']
    for produto in produtos
]

print(novos_produtos)
print(*novos_produtos, sep='\n')

novos_produtos = [
    produto
    for produto in produtos
]
print(*novos_produtos, sep='\n')

novos_produtos = [
    {'nome': produto['nome'], 'preco': produto['preco']}
    for produto in produtos
]
print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  # 5% aumento
    for produto in produtos
]
print(*novos_produtos, sep='\n')

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}  # 5% aumento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos, sep='\n')
