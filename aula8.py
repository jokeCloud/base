nome = 'Johansen'
sobrenome = 'Masterson'
idade = 19
ano_nascimento = 2022 - idade
altura_metros = 1.90


def traduz_maior_de_idade(idade):
    maior_de_idade = idade > 17
    if maior_de_idade:
        traducao = 'Sim'
    else:
        traducao = 'Não'

    return traducao


print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', traduz_maior_de_idade(idade))
print(f'Altura em metros: {altura_metros:.2f}')
