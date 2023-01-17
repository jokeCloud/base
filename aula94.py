# isinstance - saber se um objeto é de um determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'joao'},
]

for item in lista:
    if isinstance(item, int):
        print(item, isinstance(item, set))

    elif isinstance(item, float):
        print(item, isinstance(item, float))

    elif isinstance(item, str):
        print(item, isinstance(item, str))

    elif isinstance(item, bool):
        print(item, isinstance(item, bool))

    elif isinstance(item, list):
        print(item, isinstance(item, list))

    elif isinstance(item, dict):
        print(item, isinstance(item, dict))

    else:
        print('olow')
