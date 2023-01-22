import json

pessoa = {
    'nome': 'johansen',
    'sobrenome': 'masterson',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.9,
    'numeros_preferidos': (3, 6, 9, 12),
    'dev': True,
    'nada': None,
}

with open('aula125.json', 'w') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )


with open('aula125.json', 'r') as arquivo1:
    pessoa1 = json.load(arquivo1)
    print(pessoa1)
    print(type(pessoa1))
