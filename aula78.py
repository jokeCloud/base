# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor"
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc
# o valor pode ser de qualquer tipo, incluindo outro dicionário
# usamos as chaves - {} - ou a classe dict para clar dicionários
# imutáveis: str, int, float, bool, tuple
# mutável: dict, list


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
    'nome': 'nome da pessoa_1',
    'sobrenome': 'sobrenome da pessoa_1',
    'idade': 19,
    'altura': 1.90,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua tal', 'número': 456},
        {'rua': 'uma outra além da outra tal', 'número': 789},
    ]
}

print(pessoa_1, type(pessoa_1))

print(pessoa_1['sobrenome'])
print(f'número da casa: {pessoa_1["endereços"][2]["número"]}')

for chave in pessoa_1:
    print(chave, pessoa_1[chave])
