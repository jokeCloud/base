# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe

# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa_1 = {
    'nome': 'Johansen',
    'sobrenome': 'Masterson',
    'idade': 900,
}

pessoa_1.setdefault('idade', 0)
print(pessoa_1['idade'])


print(pessoa_1.__len__())
print(len(pessoa_1))

print(pessoa_1.keys())

print(tuple(pessoa_1.keys()))
print(tuple(pessoa_1.values()))

print(list(pessoa_1.keys()))
print(list(pessoa_1.values()))


for chave in pessoa_1:
    print(chave)

for chave in pessoa_1.keys():
    print(chave)

for valor in pessoa_1.values():
    print(valor)


print(list(pessoa_1.items()))

for chave, valor in pessoa_1.items():
    print(f'{chave}: {valor}')
