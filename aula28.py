"""
exercicio
peça ao seu usuário digitar seu nome
peça ao usuário digitar sua idade
se o nome e idade forem digitados:
    exiba:
        seu nome é {nome}
        seu nome investido é {nove investido}
        se o nome contém ou não espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
    se nada for digitado em nome ou idade:
        exiba "desculpe, você deixou campos vazios."
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    idade_convertida = int(idade)

    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome tem espaços em branco')
    else:
        print('Seu nome não tem espaços em branco')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A última letra do seu nome é: {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')
