"""
Introdução ao desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiza']

nome_1, nome_2, nome_3 = nomes

print(nomes)
print(nome_1, nome_2, nome_3)

primeiro_nome, *_ = ['Maria', 'Helena', 'Luiza']
_, segundo_nome, *_ = ['Maria', 'Helena', 'Luiza']

print(primeiro_nome)
print(segundo_nome)
