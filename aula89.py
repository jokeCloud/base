# empacotamento desempacotamento
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'joao',
    'sobrenome': 'michael',
}

a, b = pessoa.values()
print(a, b, type(a), type(b))

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2, b1, b2)

for chave, valor in pessoa.items():
    print(chave, valor)

dados_pessoa = {
    'idade': 16,
    'altura': 1.9,
}

print(pessoa, dados_pessoa)

# pessoa_completa = {**pessoa, 'chave': 1}
pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

pessoa_completa = {*pessoa, *dados_pessoa}

print(pessoa_completa)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoa_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)
